from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import allure
from conftest import *

import requests

payload = {
    "id": "7",
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
print(response)

