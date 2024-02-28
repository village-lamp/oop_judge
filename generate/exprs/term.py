import random


class Term:
    def __init__(self):
        self.factors = []
        self.is_negative = False

    def to_string(self, isSympy=False):
        sb = ""
        if self.is_negative:
            sb += "-"
        else:
            sb += random.choice(["+", ""])
        sb += self.factors[0].to_string(isSympy)
        for i in range(1, len(self.factors)):
            sb += "*"
            sb += self.factors[i].to_string(isSympy)
        return sb

    def clone(self):
        term = Term()
        term.factors = self.factors
        term.is_negative = self.is_negative
        return term
