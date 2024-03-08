class Number:
    def __init__(self):
        self.number = ""
        self.sympy_str = ""
        self.str = ""
        self.len = 0

    def get_cost(self):
        return self.len

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        self.sympy_str = self.number.lstrip("0")
        if self.sympy_str == "":
            self.sympy_str = "0"
        self.str = self.number
        self.len = len(self.str)
