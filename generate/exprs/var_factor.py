class VarFactor:
    def __init__(self):
        self.index = None

    def to_string(self, isSympy=False):
        sb = "x"
        if self.index is not None:
            sb += "^" + self.index.to_string(isSympy)
        return sb
