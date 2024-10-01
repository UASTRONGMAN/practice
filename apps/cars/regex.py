from enum import Enum


class CarRegex(Enum):
    MODEL = (
        r'^[A-Z][a-zA-Z]{1,49}$',
        "Model must consist of first Capital letter and only letters."
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg