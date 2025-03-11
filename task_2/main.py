import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator:
    number_strings = re.findall(r'[0-9]+\.[0-9]+', text)

    for number_string in number_strings:
        yield float(number_string)

def sum_profit(text: str, func: Callable) -> float:
    sum = 0

    for number in func(text):
        sum += number

    return sum