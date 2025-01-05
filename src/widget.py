from typing import Union
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_num: Union[str]) -> Union[str]:
    """функция скрывает номер карты и номер счета"""

    split_num = card_num.split()
    if split_num[0].lower() == "счет":
        new_split_num = "".join(split_num)
        return get_mask_account(new_split_num)
    else:
        return get_mask_card_number(card_num)


def get_date(data: Union[str]) -> Union[str]:
    """функция преобразует дату"""

    split_data = data.split("T")
    new_data = split_data[0].split("-")

    return f"{new_data[-1]}.{new_data[1]}.{new_data[0]}."
