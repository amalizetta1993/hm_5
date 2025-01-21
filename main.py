import dictionaries

levels = {
0: "Нулевой",
1: "Так себе",
2: "Можно лучше",
3: "Норм",
4: "Хорошо",
5: "Отлично"
}

words = {}

answers = {}

def get_difficulty_level():
    difficulty_levels = ['легкий', 'средний', 'тяжелый']
    level = input('Выберите уровень сложности: легкий, средний, тяжелый')
    if level not in difficulty_levels:
        level = difficulty_levels[0]
    return level

print(get_difficulty_level())