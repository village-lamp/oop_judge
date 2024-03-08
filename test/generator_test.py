from generate.exprs.expr import Expr
from generate.generator import (gen_null, gen_expr, gen_func, gen_test, gen_var_factor,
                                gen_con_factor, gen_exp_factor, gen_expr_factor, gen_term)

# var_factor = gen_var_factor(20, 200)
# print(var_factor.str, var_factor.sympy_str, var_factor.len, var_factor.get_cost())
#
# con_factor = gen_con_factor(20, 200)
# print(con_factor.str, con_factor.sympy_str, con_factor.len, con_factor.get_cost())
#
# exp_factor = gen_exp_factor(50, 5000)
# print(exp_factor.str, exp_factor.sympy_str, exp_factor.len, exp_factor.get_cost())
#
# expr_factor = gen_expr_factor(20, 200)
# print(expr_factor.str, expr_factor.sympy_str, expr_factor.len, expr_factor.get_cost())
#
# term = gen_term(50, 5000)
# print(term.str, term.sympy_str, term.len, term.get_cost())
#
# expr = gen_expr(50, 5000)
# print(expr.str, expr.sympy_str, expr.len, expr.get_cost())

for i in range(0, 50):
    out = gen_test(50, 20, 5000, 2000)
    print(out[0])
    for i in range(1, int(out[0]) + 1):
        print(out[i])
    test_expr = out[int(out[0]) + 1]
    print(test_expr.str, test_expr.sympy_str, test_expr.len, test_expr.get_cost())
i = 0
