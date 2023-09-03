from abc import ABC, abstractmethod
import requests
import json

class Api_work(ABC):
    @abstractmethod
    def upload(self):
        pass

class Hh_class(Api_work):
    def upload(self):
        print("Езда на автомобиле")

class Superjob_class(Api_work):
    def upload(self):
        print("Езда на мотоцикле")