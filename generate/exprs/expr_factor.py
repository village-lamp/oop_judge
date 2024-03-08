import random


class ExprFactor:
    def __init__(self):
        self.expr = None
        self.index = None
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        cost = max(self.expr.get_cost(), 2)
        if self.index is not None:
            cost = pow(cost, max(int(self.index.number), 1))
        return cost

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        self.sympy_str = "(" + self.expr.sympy_str + ")"
        self.str = "(" + self.expr.str + ")"
        if self.index is not None:
            c = random.choice(["+", ""])
            self.sympy_str += "^" + c + self.index.sympy_str
            self.str += "^" + c + self.index.str
        self.len = len(self.str)
