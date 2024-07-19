import aiohttp
import asyncio
import time
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

async def test_performance(add_ratio, total_operations):
    base_url = "http://localhost:8000/api/"
    headers = {'Content-Type': 'application/json'}
    note_data = {"note": "Performance Test Note", "description": "This is a test note for performance testing."}

    add_operations = int(total_operations * add_ratio)
    delete_operations = total_operations - add_operations

    add_times = []
    delete_times = []

    try:
        async with aiohttp.ClientSession() as session:
            # Add notes
            print("Добавление заметок:")
            for _ in tqdm(range(add_operations), desc="Добавление"):
                start_time = time.time()
                async with session.post(base_url + 'notes/', json=note_data, headers=headers) as response:
                    end_time = time.time()
                    add_times.append(end_time - start_time)

                    if response.status != 201:
                        print(f"Не удалось добавить заметку: {await response.json()}")


            print("Удаление заметок:")
            for note_id in tqdm(range(1, delete_operations + 1), desc="Удаление"):
                start_time = time.time()
                async with session.delete(base_url + f'notes/{note_id}/', headers=headers) as response:
                    end_time = time.time()
                    delete_times.append(end_time - start_time)

                    if response.status != 204:
                        print(f"Не удалось удалить заметку с ID {note_id}")

    except aiohttp.ClientError as e:
        print(f"Ошибка подключения к серверу: {e}")

    if add_times:
        avg_add_time = sum(add_times) / len(add_times)
        print(f"Среднее время добавления: {avg_add_time:.6f} секунд")
    else:
        avg_add_time = 0

    if delete_times:
        avg_delete_time = sum(delete_times) / len(delete_times)
        print(f"Среднее время удаления: {avg_delete_time:.6f} секунд")
    else:
        avg_delete_time = 0

    avg_time = (avg_add_time + avg_delete_time) / 2
    if avg_time <= 1.5:
        print(Fore.GREEN + "Ресурс работает в нормальном режиме.")
    else:
        print(Fore.RED + "Сайт нагружен, время ответа превышает норму.")

if __name__ == "__main__":
    while True:
        try:
            add_ratio = float(input("Введите отношение количества операций добавления к операциям удаления (0-1): "))
            if not 0 <= add_ratio <= 1:
                raise ValueError("Значение должно быть в диапазоне от 0 до 1.")
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")

    while True:
        try:
            total_operations = int(input("Введите общее количество операций: "))
            if total_operations <= 0:
                raise ValueError("Количество операций должно быть положительным числом.")
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")

    asyncio.run(test_performance(add_ratio, total_operations))
