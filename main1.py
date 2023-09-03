import json
import requests



api_key = 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
url = f'https://api.superjob.ru/2.0/vacancies/'
answer = "python"
params = {
    "keyword": answer
}

headers = {
    "X-Api-App-Id": 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)


