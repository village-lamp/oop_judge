from generate.exprs.expr import Expr
from generate.generator import gen_null, gen_expr, gen_func, gen_test

lists = gen_test(50, 20, 5000, 2000)

print(lists)
i = 1

