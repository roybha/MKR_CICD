from main import create_example_file, filter_lines_with_pandas
import os
import pytest
from pathlib import Path
import time


# Фікстура для створення тестового файлу example.txt
@pytest.fixture
def example_file():
    """Фікстура для створення тестового файлу example.txt."""
    file_name = Path("example.txt").resolve()  # Використовуємо абсолютний шлях

    # Створюємо файл з прикладом, якщо він не існує
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("Python - чудова мова програмування.\n")
            file.write("Цей рядок буде відфільтрований.\n")
            file.write("Програмування на Python дуже популярне.\n")
            file.write("Цей рядок не містить ключового слова.\n")
        print(f"Файл {file_name} створено автоматично.")
    else:
        print(f"Файл {file_name} вже існує.")

    yield file_name  # Повертаємо файл для тестів_


# Фікстура для створення та повернення файлу filtered.txt
@pytest.fixture
def filtered_file():
    """Фікстура для створення та повернення файлу filtered.txt."""
    filtered_file = Path("filtered.txt").resolve()  # Використовуємо абсолютний шлях
    yield filtered_file



# Тест для create_example_file
def test_create_example_file(example_file):
    """Тестуємо створення файлу example.txt."""
    create_example_file(example_file)
    assert os.path.exists(example_file), f"{example_file} не існує після виклику create_example_file()"


# Тест для filter_lines_with_pandas з параметризацією
@pytest.mark.parametrize("keyword, expected_lines", [
    ("Python", ["Python - чудова мова програмування.",
                "Програмування на Python дуже популярне."]),
    ("Java", []),
])
def test_filter_lines_with_pandas(example_file, filtered_file, keyword, expected_lines):
    """Тестуємо фільтрацію за допомогою pandas."""

    # Викликаємо функцію для фільтрації
    filter_lines_with_pandas(example_file, keyword, filtered_file)

    # Додаємо затримку на 0.5 секунди, щоб переконатися, що файл збережено
    time.sleep(0.5)

    # Перевіряємо, чи файл filtered.txt містить очікувані результати
    with open(filtered_file, "r", encoding="utf-8") as f:
        filtered_lines = f.readlines()

    # Очікувані результати
    expected_lines = [line + "\n" for line in expected_lines]  # Додаємо новий рядок до кожного елементу
    assert filtered_lines == expected_lines, f"Очікувані: {expected_lines}, але отримано: {filtered_lines}"



