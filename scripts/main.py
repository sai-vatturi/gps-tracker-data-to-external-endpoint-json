from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def _parse_request_data(self):
        # Parse query string parameters into a dictionary
        query_params = parse_qs(urlparse(self.path).query)

        # Convert the parsed data into a JSON-formatted string
        json_data = json.dumps(query_params, indent=2)

        return json_data

    def do_GET(self):
        # Send a response status code
        self.send_response(200)
        # Set the content type to JSON
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Parse the request data
        json_data = self._parse_request_data()

        # Print the parsed JSON data
        print(json_data)

        # Send the JSON data as the response
        self.wfile.write(json_data.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
