def get_mask_card_number(numbers: str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает номер с зашифрованными символами *"""
    numbers = str(numbers)
    new_mask_card = numbers[:4] + " " + numbers[6:8] + "** ****" + numbers[-4:]
    return new_mask_card


def get_mask_account(mask_account: str) -> str:
    """Принимает на вход номер счет в виде числа и возвращает номер счет с зашиврофарнными символами *"""
    mask_account = str(mask_account)
    new_mask_account = "**" + mask_account[-4:]
    return new_mask_account


if __name__ == "__main__":
    user_card = "5469 4201 1927 5780"
    user_count = "12345678998765432135"
    masked_info = get_mask_card_number(user_card)
    masked_count_info = get_mask_account(user_count)
    print("Зашифрованный номер карты:", masked_info)
    print("Зашифрованный номер счета:", masked_count_info)
