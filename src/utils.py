import json
from datetime import datetime


def loads_from_file(file):
    """
    Загружает из файла выполненные операции
    :param file: файл с исходними данными об операциях
    :return: список операций в формате list
    """
    with open(file, 'rt', encoding='utf-8') as f:
        return json.load(f)


def converts_date_format(original_datetime):
    formatted_datetime = datetime.fromisoformat(original_datetime)
    formatted_date = formatted_datetime.strftime("%d.%m.%Y")
    return formatted_date
