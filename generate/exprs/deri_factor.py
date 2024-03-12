class DeriFactor:
    def __init__(self):
        self.expr = None
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        return pow(2, self.len)

    def to_string(self):
        self.str = "dx(" + self.expr.str + ")"
        self.sympy_str = "diff(" + self.expr.sympy_str + ")"
        self.len = len(self.str)
