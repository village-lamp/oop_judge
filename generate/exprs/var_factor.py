import random


class VarFactor:
    default = {"x": 1, "y": 1, "z": 1}

    def __init__(self):
        self.index = None
        self.name = "x"
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        if self.index is not None:
            return pow(VarFactor.default[self.name], int(self.index.number))
        else:
            return VarFactor.default[self.name]

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        self.sympy_str = self.name
        self.str = self.name
        if self.index is not None:
            c = random.choice(["+", ""])
            self.sympy_str += "^" + c + self.index.sympy_str
            self.str += "^" + c + self.index.str
        self.len = len(self.str)
