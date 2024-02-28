import random


class ConFactor:
    def __init(self):
        self.is_negative = False
        self.number = None

    def to_string(self, isSympy=False):
        sb = ""
        if self.is_negative:
            sb += "-"
        else:
            sb += random.choice(["+", ""])
        sb += self.number.to_string(isSympy)
        return sb
