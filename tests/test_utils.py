from src.utils import converts_date_format, masks_card_number, masks_account_number


def test_converts_date_format():
    assert converts_date_format("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_masks_card_number():
    assert masks_card_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert masks_card_number("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_masks_account_number():
    assert masks_account_number("Счет 10848359769870775355") == "Счет **5355"
