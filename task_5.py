"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

#у меня макбук

import subprocess
import chardet

urls = ["yandex.ru", "youtube.com"]

for url in urls:
    ping_process = subprocess.Popen(["ping", "-c", "4", url], stdout=subprocess.PIPE)
    output, error = ping_process.communicate()
    encoding = chardet.detect(output)["encoding"]
    output = output.decode(encoding)
    print(f"Результат пинга {url}:\n{output}")
