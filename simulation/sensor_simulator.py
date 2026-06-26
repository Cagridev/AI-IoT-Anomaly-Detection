import requests
import random
import time


API_URL = "http://127.0.0.1:8000/predict"


def generate_sensor_data():

    data = {
        "temperature": random.randint(50, 100),
        "pressure": random.randint(25, 65),
        "vibration": round(random.uniform(0.1, 3.0), 2),
        "speed": random.randint(600, 1600),
        "power": random.randint(15, 60)
    }

    return data


while True:

    sensor_data = generate_sensor_data()

    response = requests.post(
        API_URL,
        json=sensor_data
    )

    result = response.json()


    print("Sensor Data:")
    print(sensor_data)

    print("AI Result:")
    print(result)

    print("-------------------")


    time.sleep(3)