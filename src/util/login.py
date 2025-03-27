import os
import requests
from getpass import getpass


def login():
    BASE_URL = os.getenv("AWS_URL")
    email = input("Email: ")
    password = getpass("Password: ")
    body = {"email": email, "password": str(password)}

    header = {"Content-Type": "application/json"}
    res = requests.post(url=BASE_URL + "/auth/login", json=body, headers=header)

    return res.json()
