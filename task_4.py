"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ["разработка", "администрирование", "protocol","standard"]
print()
# Преобразование слов в байты
byte_words = []
for word in words:
    byte_word = word.encode('utf-8')
    byte_words.append(byte_word)
    print(f"{word} в байтах: {byte_word}")
    print()
    
# Обратное преобразование байтов в слова
decoded_words = []
for byte_word in byte_words:
    decoded_word = byte_word.decode('utf-8')
    decoded_words.append(decoded_word)
    print(f"{byte_word} обратно в слово: {decoded_word}")
