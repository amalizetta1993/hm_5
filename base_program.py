#!usr/bin/env python
'''функция получения ответов от пользователя'''

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