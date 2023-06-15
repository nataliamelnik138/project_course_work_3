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
    """
    Форматирует дату
    :param original_datetime: дата в виде строки формата "2018-03-23T10:45:06.972075"
    :return: дата в виде строки формата 23.03.2018
    """
    formatted_datetime = datetime.fromisoformat(original_datetime)
    formatted_date = formatted_datetime.strftime("%d.%m.%Y")
    return formatted_date


def masks_card_number(number_card):
    """
    Маскирует номер карты
    :param number_card: исходные название и номер карты
    :return: название и замаскированный номер карты
    """
    masked_card_number = ""
    number_card_lst = number_card.split()
    for element in number_card_lst:
        if not element.isdigit():
            masked_card_number += element + " "
        else:
            for index in range(16):
                if 6 <= index <= 11:
                    if index in [7, 11]:
                        masked_card_number += "* "
                    else: masked_card_number += "*"
                else:
                    if index == 3:
                        masked_card_number += element[index] + " "
                    else:
                        masked_card_number += element[index]

    return masked_card_number
