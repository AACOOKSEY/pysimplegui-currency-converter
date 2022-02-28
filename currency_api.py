import requests

url = 'https://open.er-api.com/v6/latest/GBP'

r = requests.get(url)

response_dict = r.json()

repo_dicts = response_dict['rates']

currency = []

for k, v in repo_dicts.items():
    currency.append(k)