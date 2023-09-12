import re
from api_work import Hh_class, Superjob_class
from vacancy import Vacancy, created_hh_vacancy, Filework, created_sj_vacancy

print("Привет! Давай найдем тебе работу мечты!:)")
Filework.del_vacancy()
print("Выбери платформу на которой будем искать: если на HeadHunter - введи 1, если на Superjob - введи 2")
platform_answer = int(input())

if platform_answer == 1: #поиск вакансий на HeadHunter
    print("Введи поисковый запрос")
    key_word = str(input()).lower()
    hh = Hh_class()
    vacant = hh.get_vacancies(key_word)
    print(hh.print_vacancies(vacant))
    created_hh_vacancy(vacant)
    print("Вывести топ вакансии по зарплате? да/нет") #вывод топ по зарплате
    top_answer = str(input()).lower()
    if top_answer == 'да':
        print('Сколько топовых вакансий посмотрим?')
        top_count = int(input())
        print(Vacancy.compare_salary(top_count))
    else:
        pass
    print('Отсортируем вакансии по работодателю? да/нет') #сортировка по работодателю
    employer_answer = str(input()).lower()
    if employer_answer == 'да':
        print('Введите название работодателя')
        employer = str(input())
        print(Filework.find_vacancy(employer))
    else:
        pass
    print("Пока это все, что я умею:)")

elif platform_answer == 2: #поиск вакансий на Superjob
    print("Введи поисковый запрос")
    key_word = str(input()).lower()
    sj = Superjob_class()
    vacant = sj.get_vacancies(key_word)
    print(sj.print_vacancies(vacant))
    created_sj_vacancy(vacant)
    print("Вывести топ вакансии по зарплате? да/нет") #вывод топ по зарплате
    top_answer = str(input()).lower()
    if top_answer == 'да':
        print('Сколько топовых вакансий посмотрим?')
        top_count = int(input())
        print(Vacancy.compare_salary(top_count))
    else:
        pass
    print('Отсортируем вакансии по работодателю? да/нет') #сортировка по работодателю
    employer_answer = str(input()).lower()
    if employer_answer == 'да':
        print('Введите название работодателя')
        employer = str(input())
        print(Filework.find_vacancy(employer))
    else:
        pass
    print("Пока это все, что я умею:)")

else:
    print("Нет такой платформы, начните поиск заново")
    exit()

