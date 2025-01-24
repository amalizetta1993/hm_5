import questions

#функция выбора уровня сложности
def get_user_level(lev):
    difficulty_levels = ['легкий', 'средний', 'тяжелый'] 
    if lev not in difficulty_levels:
        lev = difficulty_levels[0]        
    print(f'Выбран {lev} уровень', end="\n\n")
    return dictionaries.dictionary[lev]

#функция получения ответов от пользователя
def base_program(dict):
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

#функция вывода правильных и неправильных слов и ранга 
def get_result(data):
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


name = input('Как вас зовут?')

level = input('Выберите уровень сложности: легкий, средний, тяжелый: ').replace(' ', '').lower()
words = get_user_level(level) #получили нужный словарь
answers = base_program(words) #получили ответы пользователя
get_result(answers) #вывод правильных и неправильных ответов и ранга

dictionary = {'легкий': words_easy, 'средний': words_medium, 'тяжелый': words_hard}