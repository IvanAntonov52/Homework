import os
from src.logging_config import BASE_DIR
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_info, get_date
from src.utils import load_operation_json
from src.processing import search_by_string, category_count, filter_by_state, sort_by_date
from src.read_transaction_file import read_csv, read_excel

if __name__ == "__main__":
    user_card = "5469420119275780"
    user_count = "12345678998765432135"
    masked_info = get_mask_card_number(user_card)
    masked_count_info = get_mask_account(user_count)
    print("Зашифрованный номер карты:", masked_info)
    print("Зашифрованный номер счета:", masked_count_info)

    cards = "Maestro 5469420119275780"
    date = "2024-03-11T02:26:18.671407"
    masked_info_name = mask_account_info(cards)
    date_info = get_date(date)
    print("Зашифрованный номер карты:", masked_info_name)
    print("Дата:", date_info)


    json_file = "operations.json"


    operations = load_operation_json(json_file)


    print(f"Загружено операций: {len(operations)}")
    if operations:
        print("Первая операция:")
        print(operations[0])



    data = load_operation_json('../data/operations.json')
    print(search_by_string(data,'Перевод организации'))


    data = load_operation_json('../data/operations.json')
    print(category_count(data, ['Перевод организации']))


    def main():
        """Отвечает за основную логику проекта и связывает функции между собой"""
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

        # 1. Выбор файла пользователя
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Пользователь: ")
        if choice == "1":
            file_path = os.path.join(BASE_DIR, "operations.json")
            transactions = load_operation_json(file_path)
            print("Для обработки выбран JSON-файл.")
        elif choice == "2":
            file_path = os.path.join(BASE_DIR, "transactions.csv")
            transactions = read_csv(file_path)
            print("Для обработки выбран CSV-файл.")
        elif choice == "3":
            file_path = os.path.join(BASE_DIR, "transactions_excel.xlsx")
            transactions = read_excel(file_path)
            print("Для обработки выбран XLSX-файл.")
        else:
            print("Неверный выбор.")
            return

        # 2. Фильтрация по статусу
        stata = ["EXECUTED", "CANCELED", "PENDING"]
        while True:
            state = (
                input(
                    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                )
                .strip()
                .upper()
            )
            if state in stata:
                print(f'Операции отфильтрованы по статусу "{state}"')
                filtered_transactions = filter_by_state(transactions, state)
                break
            else:
                print(f'Статус операции "{state}" недоступен.')

        # 3. Сортировка по дате
        sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_choice == "да":
            order_choice = input("Сортировать по возрастанию или по убыванию?\n").strip().lower()
            if order_choice == "по возрастанию":
                filtered_transactions.sort(key=lambda x: x["date"])
            elif order_choice == "по убыванию":
                filtered_transactions.sort(key=lambda x: x["date"], reverse=True)

        currency_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if currency_choice == "да":
            filtered_transactions = [
                t
                for t in filtered_transactions
                if "currency_code" in t
                   and t["currency_code"] == "RUB"
                   or "operationAmount" in t
                   and t["operationAmount"]["currency"]["code"] == "RUB"
            ]

        description_filter = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        )
        if description_filter == "да":
            search_string = input("Введите строку для поиска в описании: ")
            filtered_transactions = search_by_string(filtered_transactions, search_string)

        # 6. Вывод результатов
        print("Распечатываю итоговый список транзакций...")
        if filtered_transactions:
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
            for transaction in filtered_transactions:
                category_count(transaction)
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


    if __name__ == "__main__":
        main()