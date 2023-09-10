import json
from abc import ABC, abstractmethod
from api_work import hh


class Vacancy:

    def __init__(self, name, employer, salary, requirements, responsibility, url):
        self.name = name
        self.employer = employer
        self.salary = salary
        self.requirements = requirements
        self.responsibility = responsibility
        self.url = url

    def __dict__(self):
        return{"name": self.name,
               "employer": self.employer,
               "salary": self.salary,
               "requirements": self.requirements,
               "responsibility": self.responsibility,
               "url": self.url}

    def __str__(self):
        return self.name


    def compare_salary(self):
        pass


class FileAbsract(ABC):
    @abstractmethod
    def add_vacancy(vacancy_dict):
        pass

    @abstractmethod
    def find_vacancy(word):
        pass
    @abstractmethod
    def del_vacancy(self):
        pass


class Filework(FileAbsract):

    @staticmethod
    def add_vacancy(vacancy_dict):
        # with open('vacancy.json', 'w', encoding='utf-8') as outfile:
        content = []
        content.append(vacancy_dict.__dict__())
        with open('vacancy.json', 'w', encoding='utf-8') as outfile:
            json.dump(content, outfile, ensure_ascii=False, indent=6)

    def find_vacancy(self, word):
        file = open('vacancy.json', 'r', encoding='utf-8')
        vacancies_data = json.load(file)

        for vacancy in vacancies_data:
            if word in vacancy[0] or \
                word in vacancy[1] or\
                word in str(vacancy[2]) or\
                word in vacancy[3] or\
                word in str(vacancy[4]) or\
                word in vacancy[5]:
                return(vacancy)
            else:
                continue
        print('Нет вакансий, соответствующих заданным критериям.')

    def del_vacancy(self):
        pass


def created_hh_vacancy(vacant):
    for vacancy in vacant['items']:
        name = vacancy['name']
        employer = vacancy['employer']['name']
        if vacancy['salary']:
            salary = vacancy['salary']['from']
        else:
            salary = 0
        requirements = vacancy['snippet']['requirement']
        responsibility = vacancy['snippet']['responsibility']
        url = vacancy['alternate_url']
        vacancy_dict = Vacancy(name, employer, salary, requirements, responsibility, url)
        continue
    return (vacancy_dict)
def created_sj_vacancy(vacant):
    for vacancy in vacant['objects']:
        name = vacancy['profession']
        employer = vacancy['client']['title']
        salary = vacancy['payment_to']
        requirements = vacancy['candidat']
        responsibility = vacancy['vacancyRichText']
        url = vacancy['link']
        vacancy_dict = Vacancy(name, employer, salary, requirements, responsibility, url)
    return vacancy_dict

vacancy_dict = created_hh_vacancy(hh)
print(hh)
print(vacancy_dict)

# fw = Filework.add_vacancy(vacancy_dict)