from src.utils import converts_date_format, masks_card_number, masks_account_number, loads_from_file, filters_the_list, \
    sorts_the_list


def test_converts_date_format():
    assert converts_date_format("2018-03-23T10:45:06.972075") == "23.03.2018"


def test_masks_card_number():
    assert masks_card_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert masks_card_number("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_masks_account_number():
    assert masks_account_number("Счет 10848359769870775355") == "Счет **5355"


def test_filters_the_list():
    assert filters_the_list([{"date": "2018-02-13", "state": "EXECUTED"}, {}, {"date": "2018-02-13", "state": "CANCELED"}]) ==\
           [{"date": "2018-02-13", "state": "EXECUTED"}]

def test_sorts_the_list():
    assert sorts_the_list([{"date": "2018-02-13"}, {"date": "2018-02-23"}]) ==\
           [{"date": "2018-02-23"}, {"date": "2018-02-13"}]