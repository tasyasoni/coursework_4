from api_work import Hh_class, Superjob_class
from vacancy import Vacancy

print("Привет! Давай найдем тебе работу мечты!:)")
print("Выбери платформу на которой будем искать: если на HeadHunter - введи 1, если на Superjob - введи 2")
platform_answer = int(input())
print("Введи поисковый запрос")
key_word = str(input())

if platform_answer == 1:
    vacancy = Hh_class(key_word).get_vacancies()
    data = Vacancy(vacancy)
    data.add_vacancy()
    print("Поищем более детально? Введите ключевое слово для поиска")
    find_word = input()
    for element in data.find_vacancy(find_word):
        print(str(element))
    # print(data.find_vacancy(find_word))
elif platform_answer == 2:
    vacancy = Superjob_class(key_word).get_vacancies()
    data = Vacancy(vacancy)
    data.add_vacancy()
    print("Поищем более детально? Введите ключевое слово для поиска")
    find_word = input()
    print(data.find_vacancy(find_word))
else:
    print("Нет такой платформы, начните поиск заново")
    exit()

