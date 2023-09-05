from abc import ABC, abstractmethod
import requests
import json

class Api_work(ABC):
    @abstractmethod
    def upload(self):
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
        self.req = self.vacant['items'][0]['snippet']['requirement']
        self.salary = self.vacant['items'][0]['salary']['from']
        self.resp = self.vacant['items'][0]['snippet']['responsibility']
    def __str__(self):
        return(f'{self.name},{self.employer}, {self.salary}')

    def upload(self):
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


    def __str__(self):
        return(f'{self.name},{self.employer}, {self.salary}')

    def upload(self):
        return(self.vacant)


hh1 =  Hh_class("python")
hh2 =  Hh_class("python")
hh3 =  Hh_class("python")
hh4 =  Hh_class()
print(hh1)
print(hh2)
print(hh3)
print(hh4)

sj1 =  Superjob_class("python")
sj2 =  Superjob_class("python")
sj3 =  Superjob_class("python")
sj4 =  Superjob_class("python")
print(sj1)
print(sj2)
print(sj3)
print(sj4)

