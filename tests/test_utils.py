from src.utils import converts_date_format


def test_converts_date_format():
    assert converts_date_format("2018-03-23T10:45:06.972075") == "23.03.2018"