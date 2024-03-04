import random

from generate.exprs.con_factor import ConFactor
from generate.exprs.expr import Expr
from generate.exprs.expr_factor import ExprFactor
from generate.exprs.number import Number
from generate.exprs.term import Term
from generate.exprs.var_factor import VarFactor

isExprFactor = False


def gen_null(strs: str, times):
    for i in range(0, times):
        while True:
            pos = random.randint(-1, len(strs) - 1)
            null = random.choice([" ", "\t"])
            if pos == -1:
                strs = null + strs
                break
            if pos == len(strs) - 1:
                strs = strs + null
                break
            right = strs[pos + 1]
            left = strs[pos]
            if right.isdigit():
                if left.isdigit():
                    continue
                if left != "(" and pos != 0 and left != " " and left != "\t":
                    l_left = strs[pos - 1]
                    if not l_left.isdigit() and l_left != "x":
                        continue
            else:
                if right == "^":
                    break
            strs = strs[:pos + 1] + null + strs[pos + 1:]
            break
    return strs


def gen_expr(max_length):
    expr = Expr()
    length = 0
    while max_length - length > 2:
        length += 1
        term, lens = gen_term(random.randint(2, max_length - length))
        length += lens
        expr.add_term(term, random.choice([False, True]))
    return expr, length


def gen_term(max_length):
    term = Term()
    length = 0
    term.is_negative = random.choice([False, True])
    while max_length - length > 1:
        length += 1
        factor, lens = gen_factor(random.randint(min(max_length - length, 6),
                                                 max_length - length))
        length += lens
        term.factors.append(factor)
    return term, length


def gen_factor(max_length):
    gens = [gen_var_factor(random.randint(1, max_length))]
    if max_length > 2:
        gens.append(gen_con_factor(random.randint(2, max_length)))
    if max_length > 5 and not isExprFactor:
        gens.append(gen_expr_factor(random.randint(5, max_length)))
    factor, lens = random.choice(gens)
    return factor, lens


def gen_var_factor(max_length):
    var_factor = VarFactor()
    length = 1
    if max_length - length > 2:
        length += 1
        number, lens = gen_number(1)
        var_factor.index = number
        length += lens
    return var_factor, length


def gen_con_factor(max_length):
    con_factor = ConFactor()
    length = 1
    con_factor.is_negative = random.choice([False, True])
    number, lens = gen_number(random.randint(1, max_length - length))
    length += lens
    con_factor.number = number
    return con_factor, length


def gen_expr_factor(max_length):
    global isExprFactor
    expr_factor = ExprFactor()
    length = 1
    isExprFactor = True
    expr, lens = gen_expr(random.randint(3, max_length - 2))
    isExprFactor = False
    length += lens + 1
    expr_factor.expr = expr
    if max_length - length > 2:
        length += 1
        number, lens = gen_number(1)
        expr_factor.index = number
        length += lens
    return expr_factor, lens


def gen_number(max_length):
    number = Number()
    minn = 0
    maxx = 9 if max_length != 1 else 8
    lens = random.randint(1, min(max_length, 20))
    for i in range(0, lens):
        number.number += str(random.randint(minn, maxx))
    return number, lens
