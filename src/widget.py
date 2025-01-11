from src.masks import get_mask_account, get_mask_card_number


# Функция принимает на вход строку формата Visa Platinum 7000792289606361, или Maestro 7000792289606361,
# или Счет 73654108430135874305
def mask_account_info(card: str) -> str:
    """Определяем счет, номер и тип карты"""
    card_split = card.split()
    if "счет" in card.lower():
        return f"{card_split[0]} {get_mask_account(card_split[-1])}"
    else:
        return f"{''.join(card_split[:-1])} {get_mask_card_number(card_split[-1])}"


# Функция принимает дату и преобразовывает ее
def get_date(date_str: str) -> str:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")."""
    date_new = date_str[8:10] + "." + date_str[5:7] + "." + date_str[0:4]
    return date_new

cards = "Maestro 5469420119275780"
date = "2024-03-11T02:26:18.671407"
masked_info_name = mask_account_info(cards)
date_info = get_date(date)
print("Зашифрованный номер карты:", masked_info_name)
print("Дата:", date_info)