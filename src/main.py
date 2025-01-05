from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_card_number("Visa Platinum 7000792289606361"))
print(get_mask_card_number("Maestro 7000792289606361"))
"""маскировка номера карты"""

print(get_mask_account("Счет 73654108430135874305"))
"""маскировка номера счета"""

print(get_date("2024-03-11T02:26:18.671407"))
"""вывод даты"""

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
"""маскировка номера карты и номера счета"""
