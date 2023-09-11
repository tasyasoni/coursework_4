from api_work import Hh_class, Superjob_class
from vacancy import Vacancy, created_hh_vacancy, Filework, created_sj_vacancy

print("Привет! Давай найдем тебе работу мечты!:)")
Filework.del_vacancy(self=0)
print("Выбери платформу на которой будем искать: если на HeadHunter - введи 1, если на Superjob - введи 2")
platform_answer = int(input())

if platform_answer == 1:
    print("Введи поисковый запрос")
    key_word = input()
    hh = Hh_class()
    vacant = hh.get_vacancies(key_word)
    for vac in vacant['items']:
       print(vac['name'], vac['employer']['name'], vac['salary'], vac['url'])
    created_hh_vacancy(vacant)
    print("Вывести топ вакансии по зарплате? да/нет")
    top_answer = str(input())
    if top_answer == 'да':
        print('Сколько топовых вакансий посмотрим?')
        top_count = input()
        print(Vacancy.compare_salary(top_count))
        print("Пока это все, что я умею:)")
    else:
        print('Отсортируем вакансии по работодателю? да/нет')
        employer_answer = str(input())
        if employer_answer == 'да':
            print('Введите название работодателя')
            employer = str(input())
            print(Filework.find_vacancy(employer))
            print("Пока это все, что я умею:)")

elif platform_answer == 2:
    print("Введи поисковый запрос")
    key_word = str(input())
    sj = Superjob_class()
    vacant = sj.get_vacancies(key_word)
    for vac in vacant['objects']:
        print(vac['profession'], vac['client']['title'], vac['payment_to'], vac['link'])
    created_sj_vacancy(vacant)
    print("Вывести топ вакансии по зарплате? да/нет")
    top_answer = str(input())
    if top_answer == 'да':
        print('Сколько топовых вакансий посмотрим?')
        top_count = input()
        print(Vacancy.compare_salary(top_count))
        print("Пока это все, что я умею:)")
    else:
        print('Отсортируем вакансии по работодателю? да/нет')
        employer_answer = str(input())
        if employer_answer == 'да':
            print('Введите название работодателя')
            employer = str(input())
            print(Filework.find_vacancy(employer))
            print("Пока это все, что я умею:)")

else:
    print("Нет такой платформы, начните поиск заново")
    exit()

