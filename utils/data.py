import json
import random
from datetime import datetime, timedelta

russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

with open("utils/atms.txt", "r") as f:
    atms = json.load(f)["atms"]

for atm in atms:
    atm["workload"] = random.randint(1, 100)

    service_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    atm["service_time"] = f"{service_time.hour}:{service_time.minute}"

    car_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    on_foot_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    public_transport_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    atm["car"] = {
        "time": f"{car_time.hour}:{car_time.minute}"
    }

    atm["on_foot"] = {
        "time": f"{on_foot_time.hour}:{on_foot_time.minute}"
    }

    atm["public_transport"] = {
        "time": f"{public_transport_time.hour}:{public_transport_time.minute}"
    }

with open("utils/offices.txt", "r") as f:
    offices = json.load(f)

for office in offices:
    office["workload"] = random.randint(1, 100)

    service_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    office["service_time"] = f"{service_time.hour}:{service_time.minute}"

    car_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    on_foot_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    public_transport_time = datetime.now() + timedelta(minutes=random.randint(1, 20))

    office["car"] = {
        "time": f"{car_time.hour}:{car_time.minute}"
    }

    office["on_foot"] = {
        "time": f"{on_foot_time.hour}:{on_foot_time.minute}"
    }

    office["public transport"] = {
        "time": f"{public_transport_time.hour}:{public_transport_time.minute}"
    }