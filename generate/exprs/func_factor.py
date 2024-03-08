class FuncFactor:
    def __init__(self):
        self.var_list = []
        self.function = None
        self.sympy_str = ""
        self.str = ""
        self.len = 0
        self.cost = 0

    def get_cost(self):
        return self.cost * 2

    def to_string(self):
        self.sympy_str = ""
        self.str = ""
        self.sympy_str, self.cost = self.function.calc(self.var_list)
        self.str = self.function.name + "("
        for i in range(0, self.function.var_num):
            self.str += self.var_list[i].str + ','
        self.str = self.str.removesuffix(',')
        self.str += ")"
        self.len = len(self.str)
