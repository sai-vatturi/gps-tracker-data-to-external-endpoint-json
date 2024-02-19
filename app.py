from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
import json
import threading
import time
import os

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

config_file_path = 'config.json'

def load_config():
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default_config()
    return default_config()

def default_config():
    return {
        "external_endpoint": "https://lamas.co.in/api/sensors/dataFeed",
        "data_receive_port": 8000,
        "time_interval": 60,  # in seconds
        "last_received_location": None
    }

def save_config(config):
    with open(config_file_path, 'w') as f:
        json.dump(config, f, indent=4)

config = load_config()

def get_public_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip

def send_data_to_external_endpoint():
    while True:
        time.sleep(config['time_interval'])
        if config['last_received_location']:
            try:
                response = requests.post(config['external_endpoint'], json=config['last_received_location'], headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
                print(f'Response Status: {response.status_code}')
                print(f'Response Data: {response.text}')
            except Exception as e:
                print(f'Error sending POST request: {e}')

threading.Thread(target=send_data_to_external_endpoint, daemon=True).start()

@app.route('/currentConfig', methods=['GET'])
def current_config():
    return jsonify(config), 200

@app.route('/')
def index():
    # Convert last received location to JSON string for rendering
    last_location_str = json.dumps(config.get('last_received_location', {}))
    return render_template('config.html', last_location=last_location_str)

@app.route('/updateConfig', methods=['POST'])
def update_config_endpoint():
    global config
    data = request.json
    config.update(data)
    save_config(config)
    return jsonify(config), 200

@app.route('/getPublicIP', methods=['GET'])
def get_public_ip_route():
    return jsonify({"public_ip": get_public_ip()}), 200
@app.route('/receiveLocation', methods=['POST'])
def receive_location():
    # Ensure the entire JSON payload is stored
    config['last_received_location'] = request.json
    save_config(config)  # Save the updated configuration
    return jsonify({"status": "Location received"}), 200


if __name__ == '__main__':
    app.run(port=config['data_receive_port'], debug=True)
