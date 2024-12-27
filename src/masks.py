from typing import Union


def get_mask_card_number(card_num: Union[str]) -> Union[str]:

    """Функция скрывает часть введенного номера карты"""

    return f"{card_num [:4]} {card_num [4:6]}** **** {card_num [-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(score_bank: Union[str]) -> Union[str]:

    """Функция скрывает большую чассть номера счета"""

    return f"**{score_bank[-4:]}"


print(get_mask_account("73654108430135874305"))
