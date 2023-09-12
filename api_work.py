from abc import ABC, abstractmethod
import requests
import json


class Api_work(ABC):  #абстрактный метод для API
    @abstractmethod
    def get_vacancies(self):
        pass


class Hh_class(Api_work): #класс для получения вакансий с HeadHunter по API

    def get_vacancies(self, *answer):
        params = {
            "text": answer
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        return vacant

    def print_vacancies(self, vacant):
        """
        метод для вывода вакансий с HeadHunter на печать
        """
        for vacancy in vacant['items']:
            name = vacancy['name']
            employer = vacancy['employer']['name']
            if vacancy['salary'] ==None:
                salary = 0
            else:
                salary = vacancy['salary']['from']
            url = vacancy['alternate_url']
            print(name, employer, salary, url)


class Superjob_class(Api_work): #класс для получения вакансий c SuperJob по API

    def get_vacancies(self, *answer):
        headers = {
            "X-Api-App-Id": 'v3.r.137788648.b6e3964b060d85788bed8074f9b2410bc31ab525.9cd7dfa838ca298629103cf851f1404c23d276da'
        }
        params = {
            "keyword": answer,
        }
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        data = response.content.decode()
        vacant = json.loads(data)
        return vacant

    def print_vacancies(self, vacant):
        """
        метод для вывода вакансий с Super Job на печать
        """
        for vacancy in vacant['objects']:
            try:
                name = vacancy['profession']
                employer = vacancy['client']['title']
                salary = vacancy['payment_to']
                url = vacancy['link']
            except KeyError:
                pass
            else:
                print(name, employer, salary, url)



