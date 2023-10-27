from confluent_kafka import Producer
import requests
import json
import time

# Kafka Producer Configuration
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# API endpoints
api_url_1 = 'https://randomuser.me/api/'
api_url_2 = 'https://randomuser.me/api/'

# Periodically fetch and publish data to Kafka
while True:
    # Fetch data from API 1
    response_1 = requests.get(api_url_1)
    if response_1.status_code == 200:
        data_1 = response_1.json()
        producer.produce('api1', key='key1', value=json.dumps(data_1))
    else:
        print(f"Failed to fetch data from API 1 (Status Code: {response_1.status_code})")

    # Fetch data from API 2
    response_2 = requests.get(api_url_2)
    if response_2.status_code == 200:
        data_2 = response_2.json()
        producer.produce('api2', key='key2', value=json.dumps(data_2))
    else:
        print(f"Failed to fetch data from API 2 (Status Code: {response_2.status_code})")

    producer.flush()

    # Sleep for 20 seconds
    time.sleep(20)
