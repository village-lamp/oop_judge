from generate.exprs.var_factor import VarFactor


class Function:
    def __init__(self):
        self.name = None
        self.body = None
        self.var_num = None
        self.var_name = {}
        self.var_order = []

    def calc(self, var_list):
        res = "("
        new_var_list = []
        for i in range(0, len(var_list)):
            new_var_list.append('(' + var_list[i].sympy_str + ')')
            VarFactor.default.update({self.var_order[i]: var_list[i].get_cost()})
        cost = self.body.get_cost()
        VarFactor.default.update({"x": 1, "y": 1, "z": 1})
        last = None
        for c in self.body.sympy_str:
            if self.var_name.get(c) is not None and last != 'e':
                res += new_var_list[self.var_name.get(c)]
            else:
                res += c
            last = c
        res += ")"
        return res, cost

    def to_string(self):
        res = self.name + "("
        for i in range(0, self.var_num):
            res += self.var_order[i] + ','
        res = res.removesuffix(',')
        res += ")=" + self.body.str
        return res
