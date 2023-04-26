"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

# создаем список слов
words = ["class", "function", "method"]

# инициализируем список байтовых строк
byte_words = []

# проходим по списку слов и записываем каждое в байтовом формате
for word in words:
    byte_word = bytes(word, 'utf-8')
    byte_words.append(byte_word)

# выводим тип, содержимое и длину каждой переменной
for byte_word in byte_words:
    print(type(byte_word))
    print(byte_word)
    print(len(byte_word))
    print()
