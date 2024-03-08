import random


class Expr:
    def __init__(self):
        self.terms = []
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def add_term(self, term, is_negative):
        self.terms.append({"term": term.clone(), "is_negative": is_negative})

    def get_cost(self):
        cost = 0
        if self.str[0:1] == "-" or self.str[0:1] == "+":
            cost = 1
        for i in range(0, len(self.terms)):
            cost += self.terms[i]["term"].get_cost()
        return cost

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        if self.terms[0]["is_negative"]:
            self.sympy_str += "-"
            self.str += "-"
        else:
            c = random.choice(["+", ""])
            self.sympy_str += c
            self.str += c
        self.sympy_str += self.terms[0]["term"].sympy_str
        self.str += self.terms[0]["term"].str
        for i in range(1, len(self.terms)):
            self.sympy_str += "-" if self.terms[i]["is_negative"] else "+"
            self.str += "-" if self.terms[i]["is_negative"] else "+"
            self.sympy_str += self.terms[i]["term"].sympy_str
            self.str += self.terms[i]["term"].str
        self.len = len(self.str)
