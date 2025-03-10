    # Виджет по банковским операциям клиента

## Описание:

Виджет - помогает найти банковские операции по заданным параметрам

## Инструкции по установке:

1. Выполнить клонирование репозитория с github homework_10_2.
2. В терминале, находясь в корневой папке проекта, активировать виртуальное окружение через poetry.
3. Установить все зависимости.

## Использование разработанных функций

1. **Функция filter_by_state**:
Принимает список словарей и опционально значение для ключа 
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
state соответствует указанному значению.

**Пример входных данных для проверки функции**
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`

**Примеры работы функции**
Выход функции со статусом по умолчанию 'EXECUTED'
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]`

2.**Функция sort_by_date**:
Принимает список словарей и необязательный параметр, задающий порядок сортировки 
(по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)

**Пример входных данных для проверки функции**
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]`

**Примеры работы функции**
Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
`[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]`

### Использование функций из модуля generators.py

1. **Функция filter_by_currency**
   Функция фильтрует транзакции по заданной валюте.
   Transactions: Список словарей, представляющих транзакции.
   currency: Валюта, по которой будет происходить фильтрация

**Пример использования**

```
def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)
```

**Результат функции**

```
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
```

2. **Функция transaction_descriptions**
   Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди

**Пример использования**

```
def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]
        
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "EUR"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]
descriptions = transaction_descriptions(transactions)
for transaction in range(2):
    print(next(descriptions))
```

**Результат функции**

```
Перевод организации
Перевод со счета на счет cебе
```

3.**Функция card_number_generator**

Функция генерирующая номер карты в формате XXXX XXXX XXXX XXXX
где X — цифра номера карты. Генератор может сгенерировать номера карт в
заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999

**Пример использования**

```
def card_number_generator(start, end):
    for number in range(start, end + 1):
        # приводим номер карты в нормальный вид, по 4 цифры
        card_number = f"{number:0>16}"
        number_news = "".join([card_number[i: i + 4] + " " for i in range(0, 16, 4)])
        yield number_news.strip()


for card_number in card_number_generator(1, 6):
    print(card_number)
```

**Результат функции**

```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
0000 0000 0000 0006
```

### Использование функций из модуля decorators.py

Декоратор log, который будет автоматически логировать начало и конец выполнения функции, а также ее результаты или
возникшие ошибки.
Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут записываться логи (в файл
или в консоль)

**def log**

``` 
def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирования функций, автоматически логирует начало и конец, и результаты и возникшие ошибки"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            function_name = func.__name__
            try:
                result = func(*args, **kwargs)
                log_message = f"{function_name} ok: {result}"
            except Exception as e:
                log_message = f"{function_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise  # пробрасываем исключение дальше
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
            return result

        return wrapper

    return decorator
```

#### Пример использования декоратора

```
@log(filename="mylog.txt")
def my_function(x, y):
    """Функция суммирует 2 числа"""
    return x + y

my_function(4, 7)
```

**Результат**

```
my_function ok: 11
```

#### Пример функции с ошибкой, где на ноль делить нельзя

```
@log(filename="mylog.txt")
def my_error_function(x, y):
   return x / y

 my_error_function(1, 0)
```

**Результат**

```
my_error_function error: ZeroDivisionError. Inputs: (1, 0), {}
```


## Тестирование

Проект содержит тесты всех модулей в папках `src` и `tests`.

Отчет согласно `pytest-cov`

```
src\decorators.py               19      2    89%
src\external_api.py             26      8    69%
src\generators.py               13      0   100%
src\masks.py                    12      0   100%
src\processing.py                9      0   100%
src\utils.py                    14      3    79%
src\widget.py                   11      0   100%
tests\conftest.py               14      1    93%
tests\test_decorator.py         25      0   100%
tests\test_external_api.py      13      0   100%
tests\test_generators.py        23      0   100%
tests\test_masks.py             12      0   100%
tests\test_processing.py         7      0   100%
tests\test_utils.py             10      0   100%
tests\test_widget.py            11      0   100%
------------------------------------------------
TOTAL                          219     14    94%

```
