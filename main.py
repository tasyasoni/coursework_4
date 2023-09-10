"""Создать абстрактный класс для работы с API сайтов с вакансиями. Абстрактный класс
и классы для работы с API сайтов с вакансиями должны быть реализованы в соответствии
с принципом наследования."""


"""Реализовать классы, наследующиеся от абстрактного класса, 
для работы с конкретными платформами. Классы должны уметь подключаться к API и получать вакансии."""

""""Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты,
такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования 
и т.п. (не менее четырех) Класс должен поддерживать методы сравнения вакансий между 
собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
Класс для работы с вакансиями должен быть реализован в соответствии с принципом инкапсуляции 
и поддерживать методы сравнения вакансий между собой по зарплате.""

""""Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,"""
"""получения данных из файла по указанным критериям и удаления информации о вакансиях""

""""Создать класс для сохранения информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно"""
"""реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.""


Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем
через консоль. Самостоятельно придумать сценарии и возможности взаимодействия с пользователем.
Например, позволять пользователю указать, с каких платформ он хочет получить вакансии,
ввести поисковый запрос, получить топ N вакансий по зарплате, получить вакансии в отсортированном виде,
получить вакансии, в описании которых есть определенные ключевые слова, например "postgres" и т.п."""

import requests
import json

url = 'https://api.hh.ru/vacancies/'

answer = "Python"
params = {
    "text": answer,
    'id': None,  # ID вакансии
    'name': None,  # назввние должности
    'salary': None,  # зарплата from и to
    'type': None, #id open name Открытая
    'employer_name': None, #ID работодателя Яндекс
    'experience': None,  #нет опыта
    'employment': None,  #занятость полная_неполная
    'responsibility': None, #описание
    'requirement' : None #требования
}
req = requests.get(url, params=params)
data = req.content.decode()
vacant = json.loads(data)
for vacan in vacant:
    print(vacant['items'][0]['name'])
    print(vacant['items'][0]['employer']['name'])
    print(vacant['items'][0]['snippet']['requirement'])
    print(vacant['items'][0]['salary'])
    print(vacant['items'][0]['snippet']['responsibility'])
    print(vacant)

import json
import requests

api_key = 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
url = f'https://api.superjob.ru/2.0/vacancies/'
answer = "230000"
params = {
    "keyword": answer,
    'id_vacancy': None,  # ID вакансии
    'profession': None,  # назввние должности
    'payment_from': 100000,  # зарплата from и to
    'is_archive': False,  # id open name Открытая
    'title_client': None,  # имя работодателя
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
    print(vacant['objects'][0]['client']['title'])
    print(vacant['objects'][0]['payment_from'])
    #print(vacant)


from abc import ABC, abstractmethod
import requests
import json

class Api_work(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class Hh_class(Api_work):

    def __init__(self, *answer):
        self.answer = answer
        params = {
            "text": self.answer
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        self.vacant = vacant
        # self.name = self.vacant['items'][0]['name']
        # self.employer = self.vacant['items'][0]['employer']['name']
        # self.salary = self.vacant['items'][0]['salary']
        # self.req = self.vacant['items'][0]['snippet']['requirement']
        # self.resp = self.vacant['items'][0]['snippet']['responsibility']
        # self.url = self.vacant['items'][0]['alternate_url']

    def __str__(self):
        return(f'{self.name},\n{self.employer},\n{self.salary},\n{self.req},\n{self.resp},\n{self.url}')

    def get_vacancies(self):
        all_hh = []
        for vacancy in self.vacant['items']:
             item = (vacancy['name'], vacancy['employer']['name'], vacancy['salary'], vacancy['snippet']['requirement'], vacancy['snippet']['responsibility'], vacancy['alternate_url'])
             all_hh.append(item)
        return(all_hh)


class Superjob_class(Api_work):

    def __init__(self, *answer):
        self.answer = answer
        headers = {
            "X-Api-App-Id": 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
        }
        params = {
            "keyword": answer,
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        data = response.content.decode()
        self.vacant = json.loads(data)
        # self.name = self.vacant['objects'][0]['profession']
        # self.employer = self.vacant['objects'][0]['client']['title']
        # self.salary = self.vacant['objects'][0]['payment_to']
        # self.req = self.vacant['objects'][0]['candidat']
        # self.resp = self.vacant['objects'][0]['vacancyRichText']
        # self.url = self.vacant['objects'][0]['link']


    def __str__(self):
        return(f'{self.name},\n{self.employer},\n{self.salary},\n{self.req},\n{self.resp},\n{self.url}')

    def get_vacancies(self):
        all_sj = []
        for vacancy in self.vacant['objects']:
            item = (vacancy['profession'], vacancy['client']['title'], vacancy['payment_to'], vacancy['candidat'], vacancy ['vacancyRichText'], vacancy['link'])
            all_sj.append(item)
        return(all_sj)



# hh = Hh_class('врач').get_vacancies()
# print(hh)
#
# sj = Superjob_class("Forntend")
#
# tg = sj.get_vacancies()
# print(tg)


