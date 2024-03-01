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
   git clone https://github.com/yourgithubusername/gps-tracker-data-forwarding.git
   cd gps-tracker-data-forwarding
