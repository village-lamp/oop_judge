import random


class ExprFactor:
    def __init__(self):
        self.expr = None
        self.index = None

    def to_string(self, isSympy=False):
        sb = "("
        sb += self.expr.to_string(isSympy)
        sb += ")"
        if self.index is not None:
            sb += "^" + random.choice(["+", ""]) + self.index.to_string(isSympy)
        return sb
