import random

from generate.exprs.con_factor import ConFactor
from generate.exprs.number import Number
from generate.exprs.var_factor import VarFactor

number = Number()
number.number = "114134"
number.to_string()
print(number.len, number.get_cost(), number.str, number.sympy_str)

con_factor = ConFactor()
con_factor.is_negative = random.choice([True, False])
con_factor.number = number
con_factor.to_string()
print(con_factor.len, con_factor.get_cost(), con_factor.str, con_factor.sympy_str)

var_factor = VarFactor()
index_n = Number()
index_n.number = "8"
index_n.to_string()
var_factor.index = index_n
var_factor.name = "x"
var_factor.to_string()
print(var_factor.len, var_factor.get_cost(), var_factor.str, var_factor.sympy_str)
