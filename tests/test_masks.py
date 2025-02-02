import pytest
from src.masks import get_mask_account,get_mask_card_number

def test_get_mask_card_number() -> None:
    assert get_mask_card_number('5469420119275780') == '5469 42** **** 5780'


def test_get_mask_account() -> None:
    assert get_mask_account('12345678998765432135') == '**2135'


def test_get_mask_card_number_wrong_data() -> None:
    with pytest.raises(ValueError, match='Ошибка данных'):
        get_mask_card_number('54694201192757')


def test_get_mask_account_wrong_data() -> None:
    with pytest.raises(ValueError, match='Ошибка данных'):
        get_mask_account('1234567899876543213')