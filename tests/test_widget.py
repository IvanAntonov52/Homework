import pytest

from src.widget import get_date, mask_account_info


@pytest.mark.parametrize(
    "card, result_1",
    [
        ("Счет 12345678998765432135", "Счет 1234 **2135"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 5469420119275780", "Maestro 5469 42** **** 5780"),
    ],
)
def test_mask_account_info(card, result_1):
    assert mask_account_info(card) == result_1


def test_get_date(date_1):
    assert get_date("2024-03-11T02:26:18.671407") == date_1
    try:
        get_date("T02:26:18.671")
    except ValueError as error:
        print(error)
