import logging

masks_logger = logging.getLogger(__name__)


def get_mask_card_number(numbers: str) -> str:
    """Принимает на вход номер карты в виде числа и возвращает номер с зашифрованными символами *"""
    masks_logger.debug(
        f"Начало выполнения функции get_mask_card_number с номером: {numbers}"
    )
    numbers = str(numbers)
    if len(numbers) == 16:
        new_mask_card = numbers[:4] + " " + numbers[4:6] + "** **** " + numbers[-4:]
        masks_logger.debug(f"Маскированный номер карты: {new_mask_card}")
    else:
        error_msg = "Неверный ввод карты. Номер карты состоит из 16 чисел"
        raise ValueError(error_msg)
    return new_mask_card


def get_mask_account(mask_account: str) -> str:
    """Принимает на вход номер счет в виде числа и возвращает номер счет с зашиврофарнными символами *"""
    masks_logger.debug(
        f"Начало выполнения функции get_mask_account с номером: {mask_account}"
    )
    mask_account = str(mask_account)
    if len(mask_account) == 20:
        new_mask_account = mask_account[:4] + " " + "**" + mask_account[-4:]
        masks_logger.debug(f"Маскированный номер счета: {new_mask_account}")
    else:
        error_msg = (
            "Неверный ввод счета. Номер счета должен содержать не менее 4 символов"
        )
        masks_logger.error(error_msg)
        raise ValueError("Ошибка данных")
    return new_mask_account
