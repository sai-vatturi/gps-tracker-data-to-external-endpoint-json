# GPS Tracker Data Forwarding

This project is a Flask-based web application that receives GPS tracker data, stores it, and periodically forwards it to a specified external endpoint in JSON format. It's designed to be easily configurable and extendable for various GPS tracking needs.

## Features

- **Configuration Management:** Load, update, and save configurations from a JSON file.
- **Public IP Retrieval:** Dynamically retrieve the server's public IP address.
- **GPS Data Reception:** A dedicated endpoint to receive and store GPS location data.
- **Periodic Data Forwarding:** Automatically forward the stored GPS location data to an external endpoint at regular intervals.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   https://github.com/sai-vatturi/gps-tracker-data-to-external-endpoint-json.git
   cd gps-tracker-data-to-external-endpoint-json
   ```
2. Install Dependencies
 ```bash
   pip install Flask requests
   ```
3. Configuration
   - Edit config.json to set your external endpoint, data receive port, time interval for data forwarding, and initial last received location (if any).

4. Run the Application
    ```bash
   python app.py
   ```
   - This starts the Flask application and begins listening for GPS data on the configured port.

## Usage
### Receiving GPS Data
 - Send a POST request to /receiveLocation with the GPS data in JSON format. The application will store this data and forward it based on the configured time interval.
### Updating Configuration
 - Send a POST request to /updateConfig with the updated configuration values. This allows dynamic updating of the external endpoint, port, and other settings without restarting the service.
### Viewing and Retrieving Public IP
 - Access /getPublicIP to retrieve the current public IP address of the server hosting this service.
## API Endpoints
- GET /currentConfig - Retrieves the current configuration.
- POST /updateConfig - Updates the application configuration.
- GET /getPublicIP - Retrieves the public IP of the server.
- POST /receiveLocation - Endpoint for receiving GPS location data.
## Development
This project is open for contributions and further development. Please feel free to fork, modify, and make pull requests with new features or improvements.


