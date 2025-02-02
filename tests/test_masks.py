import pytest
from src.masks import get_mask_account,get_mask_card_number

def test_get_mask_card_number() -> None:
    assert get_mask_card_number('546942019275780') == '5469 42** **** 5780'


def test_mask_account_card_wrong_data() -> None:
    with pytest.raises(ValueError, match='Ошибка данных'):
        get_mask_card_number('54694201192757')
