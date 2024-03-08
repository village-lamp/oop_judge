import random


class ConFactor:
    def __init__(self):
        self.is_negative = False
        self.number = None
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        cost = 0
        if self.str[0] == "-" or self.str[0] == "+":
            cost = 1
        cost += self.number.get_cost()
        return cost

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        if self.is_negative:
            self.sympy_str += "-"
            self.str += "-"
        else:
            c = random.choice(["+", ""])
            self.sympy_str += c
            self.str += c
        self.sympy_str += self.number.sympy_str
        self.str += self.number.str
        self.len = len(self.str)
