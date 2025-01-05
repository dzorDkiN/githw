from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:
    """Функция скрывает часть введенного номера карты"""

    return f"{card_num [:-12]} {card_num [-12:-10]}** **** {card_num [-4:]}"


def get_mask_account(card_num: Union[str]) -> Union[str]:
    """Функция скрывает большую чассть номера счета"""

    return f"{card_num[0:4]} **{card_num[-4:]}"
