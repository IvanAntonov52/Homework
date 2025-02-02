def get_mask_card_number(numbers: str) -> str:
    """ Принимает на вход номер карты в виде числа и возвращает номер с зашифрованными символами *"""
    numbers = str(numbers)
    if len(numbers) == 16:
        new_mask_card = numbers[:4] + " " + numbers[4:6] + "** **** " + numbers[-4:]
    else:
        raise ValueError('Ошибка данных')
    return new_mask_card


def get_mask_account(mask_account: str) -> str:
    """Принимает на вход номер счет в виде числа и возвращает номер счет с зашиврофарнными символами *"""
    mask_account = str(mask_account)
    if len(mask_account) == 20:
        new_mask_account = mask_account[:4] + " " + "**" + mask_account[-4:]
    else:
        raise ValueError('Ошибка данных')
    return new_mask_account
