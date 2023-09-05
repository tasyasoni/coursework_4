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
    print(vacant['items'][0]['salary']['from'])
    print(vacant['items'][0]['snippet']['responsibility'])
    print(vacant)

