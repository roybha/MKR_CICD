"""
Варіант 3
Напишіть Python-скрипт, який зчитує вміст файлу з розширенням ".txt",
відбирає всі рядки, які містять певне ключове слово,
та записує результат у новий файл з назвою "filtered.txt".
"""
import os
import pandas as pd

def create_example_file(input_file):
    """
    Створює файл example.txt, якщо його немає.
    Додає кілька рядків як приклад.
    """
    if not os.path.exists(input_file):
        with open(input_file, "w", encoding="utf-8") as file:
            file.write("Python - чудова мова програмування.\n")
            file.write("Цей рядок буде відфільтрований.\n")
            file.write("Програмування на Python дуже популярне.\n")
            file.write("Цей рядок не містить ключового слова.\n")
        print(f"Файл {input_file} створено автоматично.")
    else:
        print(f"Файл {input_file} вже існує.")







