import random


class Term:
    def __init__(self):
        self.factors = []
        self.is_negative = False
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        cost = 1
        for i in range(0, len(self.factors)):
            cost *= self.factors[i].get_cost()
        if self.str[0:1] == "-" or self.str[0:1] == "+":
            cost += 1
        return cost

    def to_string(self):
        self.str = ""
        self.sympy_str = ""
        if self.is_negative:
            self.sympy_str += "-"
            self.str += "-"
        else:
            c = random.choice(["+", ""])
            self.sympy_str += c
            self.str += c
        self.sympy_str += self.factors[0].sympy_str
        self.str += self.factors[0].str
        for i in range(1, len(self.factors)):
            self.sympy_str += "*"
            self.str += "*"
            self.sympy_str += self.factors[i].sympy_str
            self.str += self.factors[i].str
        self.len = len(self.str)

    def clone(self):
        term = Term()
        term.factors = self.factors
        term.is_negative = self.is_negative
        term.str = self.str
        term.sympy_str = self.sympy_str
        term.len = self.len
        return term
