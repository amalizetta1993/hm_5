#!usr/bin/env python
'''функция выбора уровня сложности'''

import json
def get_user_level(lev):
    dictionary = {'легкий': 0, 'средний': 1, 'тяжелый': 2}
    with open("questions.json", "r", encoding = 'utf-8') as fh:
        data = json.load(fh, ) # записываем структуру в файл
        if lev not in dictionary:
            lev = 'легкий'       
        print(f'Выбран {lev} уровень', end="\n\n")
        
    dic = data[0]['questions'][dictionary[lev]] 
        
    return dic

