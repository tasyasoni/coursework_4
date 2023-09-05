from api_work import choise, choisegj


class Vacancy:
    def __init__(self, vacant):
        self.vacancy_name = vacancy_name
        self.vacancy_employer = vacancy_employer
        self.vacancy_salary = vacancy_salary
        self.vacancy_experience = vacancy_experience
        self.vacancy_requirement = vacancy_requirement
        self.vacancy_responsibility = vacancy_responsibility
        self.vacancy_url = vacancy_url

    def __str__(self):
        return (f'{self.vacancy_name}')

    def compare_salary(self):
        pass



result = Vacancy(choise)
print(result)

resultgj = Vacancy(choisegj)
print(resultgj)