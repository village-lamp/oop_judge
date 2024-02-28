class Number:
    def __init__(self):
        self.number = ""

    def to_string(self, isSympy=False):
        return self.number if not isSympy else self.number.lstrip("0")
