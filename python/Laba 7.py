# Импорт необходимых модулей
import datetime  # Для работы с датой и временем
import time  # Для измерения времени выполнения и задержек
from functools import wraps  # Декоратор wraps для сохранения метаданных функций


# 1. Декоратор для логирования вызовов функций в файл
def log_decorator(func):
    @wraps(func)  # Сохраняет оригинальные атрибуты функции
    def wrapper(*args, **kwargs):
        # Фиксируем время начала выполнения функции
        start_time = datetime.datetime.now()
        # Форматируем время начала в строку заданного формата
        start_time_str = start_time.strftime("[%Y-%m-%d %H:%M:%S]")

        # Замеряем время выполнения с помощью time.time()
        start = time.time()
        # Вызываем оригинальную функцию с переданными аргументами
        result = func(*args, **kwargs)
        end = time.time()
        # Вычисляем время выполнения (разница между end и start)
        execution_time = end - start

        # Фиксируем время завершения функции
        end_time = datetime.datetime.now()
        # Форматируем время завершения
        end_time_str = end_time.strftime("[%Y-%m-%d %H:%M:%S]")

        # Формируем запись для лог-файла:
        # 1. Время вызова и имя функции с аргументами
        # 2. Время завершения, время выполнения и результат
        log_entry = (
            f"{start_time_str} Функция '{func.__name__}' вызвана с аргументами: {args}, {kwargs}\n"
            f"{end_time_str} Функция '{func.__name__}' завершена. "
            f"Время выполнения: {execution_time:.2f} сек. Результат: {result!r}.\n\n"
        )

        # Открываем файл для добавления записей (режим 'a')
        # Используем encoding='utf-8' для корректной работы с русским языком
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)  # Записываем сформированную строку в файл

        return result  # Возвращаем результат оригинальной функции

    return wrapper  # Возвращаем функцию-обертку


# 2. Декоратор для ограничения количества вызовов функции
def rate_limit(max_calls, period):
    # Внешняя функция-фабрика декоратора
    def decorator(func):
        calls = []  # Список для хранения временных меток вызовов

        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def wrapper(*args, **kwargs):
            # Получаем текущее время
            current_time = time.time()
            # Фильтруем список вызовов, оставляя только те,
            # которые были в течение последних 'period' секунд
            calls[:] = [call for call in calls if call > current_time - period]

            # Если количество вызовов превысило лимит
            if len(calls) >= max_calls:
                print("Превышен лимит вызовов. Попробуйте позже.")
                return None  # Возвращаем None вместо вызова функции

            # Добавляем текущее время в список вызовов
            calls.append(current_time)
            # Вызываем оригинальную функцию
            return func(*args, **kwargs)

        return wrapper  # Возвращаем функцию-обертку

    return decorator  # Возвращаем декоратор


# 3. Декоратор для кэширования результатов функции
def cache_decorator(func):
    cache = {}  # Словарь для хранения кэшированных результатов

    @wraps(func)  # Сохраняем метаданные оригинальной функции
    def wrapper(*args, **kwargs):
        # Создаем ключ на основе позиционных и именованных аргументов
        # frozenset используется для именованных аргументов, так как он хешируемый
        key = (args, frozenset(kwargs.items()))

        # Если результат для данного ключа еще не в кэше
        if key not in cache:
            # Вычисляем и сохраняем результат
            cache[key] = func(*args, **kwargs)

        # Возвращаем результат из кэша
        return cache[key]

    return wrapper  # Возвращаем функцию-обертку


# Пример функции с декоратором логирования
@log_decorator
def calculate_power(base, exponent):
    """Возводит число в степень"""
    time.sleep(1)  # Искусственная задержка для демонстрации
    return base ** exponent  # Возвращаем результат возведения в степень


# Пример функции с декоратором ограничения вызовов
@rate_limit(max_calls=3, period=10)
def send_notification(message):
    """Отправляет уведомление"""
    print(f"Отправлено уведомление: {message}")


# Пример функции с декоратором кэширования
@cache_decorator
def fibonacci(n):
    """Вычисляет число Фибоначчи"""
    if n <= 1:  # Базовый случай рекурсии
        return n
    # Рекурсивный вызов с сохранением промежуточных результатов в кэше
    return fibonacci(n - 1) + fibonacci(n - 2)


# Демонстрация работы всех декораторов
if __name__ == "__main__":
    print("=== Демонстрация декоратора логирования ===")
    print(calculate_power(2, 10))  # Результат запишется в log.txt

    print("\n=== Демонстрация декоратора ограничения вызовов ===")
    for i in range(5):  # Пытаемся вызвать функцию 5 раз
        send_notification(f"Тест {i + 1}")  # Но сработает только 3 раза за 10 секунд
        time.sleep(1)  # Пауза между вызовами

    print("\n=== Демонстрация декоратора кэширования ===")
    print("fibonacci(10):", fibonacci(10))  # Будет вычислено
    print("fibonacci(10):", fibonacci(10))  # Возьмется из кэша
    print("fibonacci(15):", fibonacci(15))  # Частично использует кэш
