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

def filter_lines_with_pandas(input_file, keyword, output_file="filtered.txt"):
    """
    Метод, що буде фільтрувати текст вхідного файлу за допомогою pandas.
    Результати записуються у filtered.txt, якщо рядок містить ключове слово.
    """
    try:
        # Створюємо файл example.txt, якщо він не існує
        create_example_file(input_file)

        # Читання вхідного файлу як простого тексту за допомогою pandas
        df = pd.read_csv(input_file, header=None, names=["Line"], encoding="utf-8")

        # Фільтруємо рядки, що містять ключове слово
        filtered_df = df[df['Line'].str.contains(keyword, na=False)]

        # Запис результатів у вихідний файл
        filtered_df.to_csv(output_file, index=False, header=False, encoding="utf-8")

        print(f"Фільтрація завершена. Результати записані у {output_file}")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

# Запуск скрипта
input_filename = "example.txt"
keyword_to_search = "Python"
filter_lines_with_pandas(input_filename, keyword_to_search)






