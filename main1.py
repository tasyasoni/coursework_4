import json
import requests

api_key = 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
url = f'https://api.superjob.ru/2.0/vacancies/'
answer = "230000"
params = {
    "keyword": answer,
    'id_vacancy': None,  # ID вакансии
    'profession': None,  # назввние должности
    'address': None,  # страна Россия 113
    'payment_to': 100000,  # зарплата from и to
    'is_archive': False,  # id open name Открытая
    'id_client': None,  # ID работодателя Яндекс
    'experience': None,  # нет опыта
    'type_of_work': None,  # занятость полная_неполная
    'vacancyRichText': None,  # описание
    'candidat': None  # требования
}

headers = {
    "X-Api-App-Id": 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
}

response = requests.get(url, headers=headers, params=params)
data = response.content.decode()
vacant = json.loads(data)
for data in vacant:
    print(vacant['objects'][0]['profession'])
    print(vacant['objects'][0]['candidat'])
    print(vacant['objects'][0]['payment_to'])

