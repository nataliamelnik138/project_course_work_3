from src.utils import loads_from_file, converts_date_format, masks_account_number, masks_card_number, sorts_the_list, \
    filters_the_list

FILE = 'operations.json'
def main():
    # Список всех операций
    all_operations = loads_from_file(FILE)
    # Отфильтрованный список операций
    operation_filters = filters_the_list(all_operations)
    # Отсортированный список операций
    operations = sorts_the_list(operation_filters)

    # Вывод 5 последних выполненных операций
    for index in range(5):
        # Форматируем дату операции
        date_operation = converts_date_format(operations[index]["date"])
        # Описание типа перевода
        transfer_description = operations[index]["description"]
        # Откуда перевод
        if "from" in operations[index].keys():
            where_transfer_from = operations[index]["from"]
            if "Счет" in where_transfer_from:
                masks_where_transfer_from = masks_account_number(where_transfer_from)
            else:
                masks_where_transfer_from = masks_card_number(where_transfer_from)
        else:
            masks_where_transfer_from = ""
        # Куда перевод
        where_transfer = operations[index]["to"]
        if "Счет" in where_transfer:
            masks_where_transfer = masks_account_number(where_transfer)
        else:
            masks_where_transfer = masks_card_number(where_transfer)
        # Сумма и валюта перевода
        amount_transfer = operations[index]["operationAmount"]["amount"]
        currency_transfer = operations[index]["operationAmount"]["currency"]["name"]

        print(f"{date_operation} {transfer_description}")
        print(f"{masks_where_transfer_from} -> {masks_where_transfer}")
        print(f"{amount_transfer} {currency_transfer}\n")


if __name__ == '__main__':
    main()
