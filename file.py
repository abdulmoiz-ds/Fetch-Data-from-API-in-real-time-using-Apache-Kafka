from confluent_kafka import Producer
import requests
import json
import time
from datetime import datetime

# Kafka Producer Configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# API endpoints
api_url_1 = 'https://randomuser.me/api/'
api_url_2 = 'https://randomuser.me/api/'

# Initialize data containers
data_1 = []
data_2 = []

while True:
    # Fetch data from API 1
    response_1 = requests.get(api_url_1)
    if response_1.status_code == 200:
        data_1.append(response_1.json())
    else:
        print(f"Failed to fetch data from API 1 (Status Code: {response_1.status_code})")

    # Fetch data from API 2
    response_2 = requests.get(api_url_2)
    if response_2.status_code == 200:
        data_2.append(response_2.json())
    else:
        print(f"Failed to fetch data from API 2 (Status Code: {response_2.status_code})")

    # Save data to JSON files every 20 seconds
    if len(data_1) > 0:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f'api1_data_{timestamp}.json', 'w') as file:
            json.dump(data_1, file)
        data_1 = []  # Clear the data

    if len(data_2) > 0:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        with open(f'api2_data_{timestamp}.json', 'w') as file:
            json.dump(data_2, file)
        data_2 = []  # Clear the data

    # Sleep for 20 seconds
    time.sleep(20)
