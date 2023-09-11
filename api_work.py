from abc import ABC, abstractmethod
import requests
import json


class Api_work(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class Hh_class(Api_work):

    def get_vacancies(self, *answer):
        params = {
            "text": answer
        }
        req = requests.get('https://api.hh.ru/vacancies/', params=params)
        data = req.content.decode()
        vacant = json.loads(data)
        return vacant


class Superjob_class(Api_work):

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





