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

