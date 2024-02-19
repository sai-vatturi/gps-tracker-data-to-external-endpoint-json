#!/usr/bin/env python3

import sys
import math
import urllib
import http.client as httplib
import time
import random
import json
import http.client

id = '132456789012345'
server = 'localhost:8000'
period = 1
step = 0.001
device_speed = 40
driver_id = '123456'

waypoints = [
    (48.853780, 2.344347),
    (48.855235, 2.345852),
    (48.857238, 2.347153),
    (48.858509, 2.342563),
    (48.856066, 2.340432),
    (48.854780, 2.342230)
]

points = []

for i in range(0, len(waypoints)):
    (lat1, lon1) = waypoints[i]
    (lat2, lon2) = waypoints[(i + 1) % len(waypoints)]
    length = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    count = int(math.ceil(length / step))
    for j in range(0, count):
        lat = lat1 + (lat2 - lat1) * j / count
        lon = lon1 + (lon2 - lon1) * j / count
        points.append((lat, lon))

def send(conn, lat, lon, altitude, course, speed, battery, alarm, ignition, accuracy, rpm, fuel, driverUniqueId):
    data = {
        "id": id,
        "timestamp": int(time.time()),
        "lat": lat,
        "lon": lon,
        "altitude": altitude,
        "bearing": course,
        "speed": speed,
        "battery": battery,
        "alarm": "sos" if alarm else None,
        "ignition": ignition,
        "accuracy": accuracy,
        "rpm": rpm,
        "fuel": fuel,
        "driverUniqueId": driverUniqueId
    }
    
    headers = {'Content-Type': 'application/json'}
    conn.request('POST', '/receiveLocation', body=json.dumps(data), headers=headers)
    response = conn.getresponse()
    print(response.status, response.reason, response.read().decode())

# Assuming 'server' is defined as 'localhost:8000'
def course(lat1, lon1, lat2, lon2):
    lat1 = lat1 * math.pi / 180
    lon1 = lon1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    lon2 = lon2 * math.pi / 180
    y = math.sin(lon2 - lon1) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
    return (math.atan2(y, x) % (2 * math.pi)) * 180 / math.pi

index = 0

conn = http.client.HTTPConnection(server)

while True:
    (lat1, lon1) = points[index % len(points)]
    (lat2, lon2) = points[(index + 1) % len(points)]
    altitude = 50
    speed = device_speed if (index % len(points)) != 0 else 0
    alarm = (index % 10) == 0
    battery = random.randint(0, 100)
    ignition = (index / 10 % 2) != 0
    accuracy = 100 if (index % 10) == 0 else 0
    rpm = random.randint(500, 4000)
    fuel = random.randint(0, 80)
    driverUniqueId = driver_id if (index % len(points)) == 0 else False
    send(conn, lat1, lon1, altitude, course(lat1, lon1, lat2, lon2), speed, battery, alarm, ignition, accuracy, rpm, fuel, driverUniqueId)
    time.sleep(period)
    index += 1
