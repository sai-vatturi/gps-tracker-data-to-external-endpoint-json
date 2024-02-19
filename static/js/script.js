document.addEventListener('DOMContentLoaded', function() {
    fetch('/currentConfig')
    .then(response => response.json())
    .then(data => {
        document.getElementById('endpoint').value = data.external_endpoint;
        document.getElementById('interval').value = data.time_interval;
        
        // Debugging line to see what's being fetched
        console.log("Last Location Data: ", data.last_received_location);

        // Display the last received location if it exists
        var lastLocationData = document.getElementById('lastLocation').textContent;
        console.log("Last Location Data from Element: ", lastLocationData); // Debugging line
        if (lastLocationData) {
            var formattedData = JSON.stringify(JSON.parse(lastLocationData), null, 2); // Pretty print the JSON
            document.getElementById('lastLocation').textContent = formattedData;
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('configForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const endpoint = document.getElementById('endpoint').value;
    const interval = document.getElementById('interval').value;

    fetch('/updateConfig', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ external_endpoint: endpoint, time_interval: parseInt(interval) }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Configuration updated!');
        console.log(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('getIPButton').addEventListener('click', function() {
    fetch('/getPublicIP')
    .then(response => response.json())
    .then(data => {
        document.getElementById('publicIP').textContent = `Public IP: ${data.public_ip}`;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
