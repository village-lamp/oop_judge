class Number:
    def __init__(self):
        self.number = ""

    def to_string(self, isSympy=False):
        if isSympy:
            self.number = self.number.lstrip("0")
            if self.number == "":
                self.number = "0"
        return self.number
