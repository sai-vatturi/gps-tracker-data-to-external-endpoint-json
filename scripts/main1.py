from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
import http.client

class RequestHandler(BaseHTTPRequestHandler):
    def _parse_request_data(self):
        # Parse query string parameters into a dictionary
        query_params = parse_qs(urlparse(self.path).query)

        # Convert the parsed data into a JSON-formatted string
        json_data = json.dumps(query_params, indent=2)

        return json_data

    def do_GET(self):
        # Parse the request data
        json_data = self._parse_request_data()

        # Define the external endpoint URL
        external_endpoint = 'lamas.co.in'
        path = '/api/sensors/dataFeed'

        # Create a connection to the external server
        conn = http.client.HTTPSConnection(external_endpoint)

        # Set headers for the POST request
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # Send a POST request to the external endpoint
        try:
            conn.request('POST', path, json_data, headers)
            response = conn.getresponse()

            # Print the response status and read the response data
            print(f'Response Status: {response.status}')
            response_data = response.read().decode('utf-8')
            print(f'Response Data: {response_data}')
        except Exception as e:
            print(f'Error sending POST request: {e}')
        finally:
            # Close the connection
            conn.close()

if __name__ == '__main__':
    # Run the server on port 8000
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()
