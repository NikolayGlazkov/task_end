words = ['питон', 'тру', 'язык']  # список слов

for word in words:
    # каждое слово разбиваем на буквы
    print(f'Слово "{word}" в буквенном формате:', list(word))

    # Набор кодовых точек
    code_points = [f'\\u{ord(c):04x}' for c in word]
    code_points_str = ''.join(code_points)
    print(f'Слово "{word}" в наборе кодовых точек:', code_points_str)

    # Проверка типа и содержания переменной
    print(f'Тип переменной {word}: {type(word)}, содержание: {word}')
    print()
