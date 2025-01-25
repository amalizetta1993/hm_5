import get_result, base_program, get_user_level
   
print('''
      Привет! Это приложение для проверки знаний английского языка.
                Переведи слова с английского на русский

''')

name = input('Как вас зовут? ')
level = input('Выберите уровень сложности: легкий, средний, тяжелый: ').replace(' ', '').lower()

words = get_user_level.get_user_level(level) #получили нужный словарь
answers = base_program.base_program(words) #получили ответы пользователя
get_result.get_result(answers, name) #вывод правильных и неправильных ответов и ранга
