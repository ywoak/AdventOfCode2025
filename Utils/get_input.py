from dotenv import load_dotenv
import requests
import sys
import os

load_dotenv()

num: str = sys.argv[1]
input_url: str = f'https://adventofcode.com/2025/day/{num}/input'

cookie_name: str = 'session'
cookie_value: str | None = os.getenv('COOKIE_VALUE')

if cookie_value is None:
    raise RuntimeError('COOKIE_VALUE non défini, il vous manque le .env')

r: requests.Response = requests.get(input_url, cookies={cookie_name: cookie_value})

with open(f'input_{num}.txt', 'w') as file:
    file.write(r.text)
