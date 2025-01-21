import dictionaries

levels = {
0: "Нулевой",
1: "Так себе",
2: "Можно лучше",
3: "Норм",
4: "Хорошо",
5: "Отлично"
}

answers = {}

#функция выбора уровня
def get_difficulty_level():
    difficulty_levels = ['легкий', 'средний', 'тяжелый']
    level = input('Выберите уровень сложности: легкий, средний, тяжелый: ').replace(' ', '').lower()
    if level not in difficulty_levels:
        level = difficulty_levels[0]
    return level

print('''Привет! Это приложение для проверки знаний английского языка.
Переведи слова с английского на русский''')

words = dictionaries.dictionary[get_difficulty_level()] #выбрали уровень сложности и получили нужный словарь
