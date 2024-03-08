import random


class ExpFactor:
    def __init__(self):
        self.factor = None
        self.index = None
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        if self.index is not None:
            return pow(2, int(self.index.number)) + self.factor.get_cost() + 1
        else:
            return self.factor.get_cost() + 1

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        self.sympy_str = "exp(" + self.factor.sympy_str + ")"
        self.str = "exp(" + self.factor.str + ")"
        if self.index is not None:
            c = random.choice(["+", ""])
            self.sympy_str += "^" + c + self.index.sympy_str
            self.str += "^" + c + self.index.str
        self.len = len(self.str)
