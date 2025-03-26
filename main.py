from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_info, get_date
from src.utils import load_operation_json


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
