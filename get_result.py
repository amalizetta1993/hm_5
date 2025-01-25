#!usr/bin/env python
'''функция вывода правильных и неправильных слов и ранга'''
import json
def get_result(data,user):
    right_words = []
    wrong_words = []
    for key, value in data.items():
        right_words.append(key) if value else wrong_words.append(key)
    print()   
    print('Правильно отвечены слова:', end = '\n')  
    print(*right_words, sep='\n', end="\n\n")
    print('Неправильно отвечены слова:', end = '\n')  
    print(*wrong_words, sep='\n', end="\n\n")
    with open("questions.json", "r", encoding = 'utf-8') as fh:
        d = json.load(fh, ) # записываем структуру в файл
        rang = d[1]['levels'][str(len(right_words))]    
        print(f'Ваш ранг: \n {rang}')                 
    result = {"Имя пользователя":user,
        "Правильно отвеченные слова":right_words,
        "Неправильно отвеченые слова:":wrong_words,
        "Ранг":rang}
    d = json.dumps(result, ensure_ascii = False, indent = 4)
    with open("result.json", "w", encoding = 'utf-8') as fh1:
        fh1.write(d) # записываем структуру в файл
        
