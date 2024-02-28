import random


class Expr:
    def __init__(self):
        self.terms = []

    def add_term(self, term, is_negative):
        self.terms.append({"term": term.clone(), "is_negative": is_negative})

    def to_string(self, isSympy=False):
        sb = ""
        if self.terms[0]["is_negative"]:
            sb += "-"
        else:
            sb += random.choice(["+", ""])
        sb += self.terms[0]["term"].to_string(isSympy)
        for i in range(1, len(self.terms)):
            sb += "-" if self.terms[i]["is_negative"] else "+"
            sb += self.terms[i]["term"].to_string(isSympy)
        return sb
