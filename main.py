import dictionaries

#функция выбора уровня сложности
def get_difficulty_level():
    difficulty_levels = ['легкий', 'средний', 'тяжелый']
    level = input('Выберите уровень сложности: легкий, средний, тяжелый: ').replace(' ', '').lower()
    print()
    if level not in difficulty_levels:
        level = difficulty_levels[0]
        
    print(f'Выбран {level} уровень', end="\n\n")
    return level

#функция получения ответов от пользователя
def get_answers(dict):
    users_answers = {}
    for key, value in dict.items():
        answer = input(f'{key}, {len(value)} букв(а), начинается на {value[0]}...')
        if answer == value:
            print(f'Верно, {key} — это {value}.')
            users_answers[key] = True
        else:
            print(f'Неверно, {key} — это {value}.')
            users_answers[key] = False
    return users_answers

#функция вывода правильных и неправильных слов   
def print_answers_and_rang(data):
    levels = {
                0: "Нулевой",
                1: "Так себе",
                2: "Можно лучше",
                3: "Норм",
                4: "Хорошо",
                5: "Отлично"
            }
    right_words = set()
    wrong_words = set()
    for key, value in data.items():
        right_words.add(key) if value else wrong_words.add(key)
    print()   
    print('Правильно отвечены слова:', end = '\n')  
    print(*right_words, sep='\n', end="\n\n")
    print('Неправильно отвечены слова:', end = '\n')  
    print(*wrong_words, sep='\n', end="\n\n")        
    print(f'Ваш ранг: \n {levels[len(right_words)]}')                 
#########################################################################################
   
print('''
      Привет! Это приложение для проверки знаний английского языка.
                Переведи слова с английского на русский
''')

words = dictionaries.dictionary[get_difficulty_level()] #выбрали уровень сложности и получили нужный словарь

answers = get_answers(words) #получили ответы пользователя
print_answers_and_rang(answers) #вывод правильных и неправильных ответов и ранга