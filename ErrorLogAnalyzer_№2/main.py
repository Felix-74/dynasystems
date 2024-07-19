import re
from collections import Counter


class ErrorLogAnalyzer:
    """
    Класс для анализа лог файла на наличие кодов ошибок.

    Атрибуты:
    log_file : str
        Путь к лог файлу.
    error_counts : collections.Counter
        Счетчик, содержащий количество вхождений каждого кода ошибки.

    Методы:
    analyze():
        Читает лог файл и подсчитывает коды ошибок.
    get_sorted_error_counts():
        Возвращает отсортированный список кодов ошибок и их количество.
    print_sorted_error_counts():
        Выводит отсортированный список кодов ошибок и их количество на экран.
    """

    def __init__(self, log_file):
        """
        Инициализируем класс ErrorLogAnalyzer с путем к лог файлу.

        Параметры:
        log_file : str
            Путь к лог файлу.
        """
        self.log_file = log_file
        self.error_counts = Counter()

    def analyze(self):
        """
        Читает содержимое лог файла и подсчитывает уникальные коды ошибок.

        Типы исключений:
        FileNotFoundError:
            Если лог файл не найден.
        ValueError:
            Если лог файл пустой.
        """
        try:
            with open(self.log_file, 'r') as file:
                log_content = file.read()

            if not log_content.strip():
                raise ValueError("Лог пустой")

            error_codes = re.findall(r'\b\w{5}\b', log_content)

            if not error_codes:
                raise ValueError("Не найдено кодов ошибок в лог файле")

            self.error_counts = Counter(error_codes)

        except FileNotFoundError:
            print(f"Ошибка: Файл '{self.log_file}' не найден.")
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

    def get_sorted_error_counts(self):
        """
        Возвращает отсортированный список кодов ошибок и их количество.
        """
        return sorted(self.error_counts.items(), key=lambda x: x[1], reverse=True)

    def print_sorted_error_counts(self):
        """
        Выводит отсортированный список кодов ошибок и их количество на экран.
        """
        sorted_error_counts = self.get_sorted_error_counts()

        if not sorted_error_counts:
            print("Нет данных для отображения.")
            return

        for code, count in sorted_error_counts:
            print(f"{code} : {count}")


# Пример использования
log_file = 'log.txt'
analyzer = ErrorLogAnalyzer(log_file)
analyzer.analyze()
analyzer.print_sorted_error_counts()
