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
        self.name = self.vacant['items'][0]['name']
        self.employer = self.vacant['items'][0]['employer']['name']
        self.salary = self.vacant['items'][0]['salary']['from']
        self.req = self.vacant['items'][0]['snippet']['requirement']
        self.resp = self.vacant['items'][0]['snippet']['responsibility']
        self.url = self.vacant['items'][0]['alternate_url']
    def __str__(self):
        return(f'{self.name},\n{self.employer},\n{self.salary},\n{self.req},\n{self.resp},\n{self.url}')

    def get_vacancies(self):
        return(self.vacant)


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
        self.name = self.vacant['objects'][0]['profession']
        self.employer = self.vacant['objects'][0]['client']['title']
        self.salary = self.vacant['objects'][0]['payment_to']
        self.req = self.vacant['objects'][0]['candidat']
        self.resp = self.vacant['objects'][0]['vacancyRichText']
        self.url = self.vacant['objects'][0]['link']


    def __str__(self):
        return(f'{self.name},\n{self.employer},\n{self.salary},\n{self.req},\n{self.resp},\n{self.url}')

    def get_vacancies(self):
        return(self.vacant)


choise = Hh_class("врач")
print(choise)


choisegj = Superjob_class('учитель')
print(choisegj)