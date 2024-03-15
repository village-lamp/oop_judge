import math
import random

from generate.exprs.con_factor import ConFactor
from generate.exprs.deri_factor import DeriFactor
from generate.exprs.exp_factor import ExpFactor
from generate.exprs.expr import Expr
from generate.exprs.expr_factor import ExprFactor
from generate.exprs.func_factor import FuncFactor
from generate.exprs.number import Number
from generate.exprs.term import Term
from generate.exprs.var_factor import VarFactor
from generate.util.function import Function

functions = []
var_lists = []
max_func_cost = 0
is_func = 0
is_strong = False


def gen_test(max_length, func_max_length, max_cost, func_max_cost, strong):
    global functions, max_func_cost, is_strong
    is_strong = strong
    res = []
    max_func_cost = 0
    functions = []
    func_name = ['f', 'g', 'h']
    random.shuffle(func_name)
    func_num = random.randint(0, 3)
    res.append(str(func_num))
    for i in range(0, func_num):
        function = gen_func(func_name[i], func_max_length, func_max_cost)
        functions.append(function)
        res.append(function.to_string())
        _, cost = function.calc([VarFactor(), VarFactor(), VarFactor()])
        max_func_cost = max(max_func_cost, cost)
    max_func_cost *= 2
    expr = gen_expr(max_length, max_cost)
    res.append(expr.str)
    res.append(expr.sympy_str)
    return res


def gen_func(func_name, max_length, max_cost):
    global is_func, var_lists
    function = Function()
    function.name = func_name
    function.var_num = random.randint(1, 3)
    var_name = ['x', 'y', 'z']
    random.shuffle(var_name)
    function.var_order = var_name[0:function.var_num]
    for i in range(0, function.var_num):
        function.var_name.update({var_name[i]: i})
    is_func = function.var_num
    var_lists = function.var_order
    function.body = gen_expr(max_length, max_cost)
    var_lists = []
    is_func = 0
    return function


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


def gen_expr(max_length, max_cost):
    expr = Expr()
    length = 0
    while max_length - length > 2:
        if not is_strong and expr.get_cost() + 2 >= max_cost:
            break
        length += 1
        term = gen_term(max_length - length, max_cost - expr.get_cost())
        length += term.len
        expr.add_term(term, random.choice([False, True]))
    expr.to_string()
    return expr


def gen_term(max_length, max_cost):
    term = Term()
    length = 0
    term.is_negative = random.choice([False, True])
    while max_length - length > 1:
        if not is_strong and term.get_cost() >= max_cost:
            break
        length += 1
        factor = gen_factor(max_length - length, max_cost // term.get_cost())
        length += factor.len
        term.factors.append(factor)
        if random.randint(0, 1) > 0:
            break
    term.to_string()
    return term


def gen_factor(max_length, max_cost):
    gens = [gen_var_factor]
    if is_strong:
        max_cost = max_func_cost + 100
    if max_length > 2 and max_cost > 1:
        gens.append(gen_con_factor)
    if max_length > 4 and max_cost > 10:
        gens.append(gen_expr_factor)
    if max_length > 7 and max_cost > 10:
        gens.append(gen_exp_factor)
    if max_length > 7 and len(functions) > 0 and max_cost > max_func_cost:
        gens.append(gen_func_factor)
    if max_length > 6 and max_cost > 10 and not is_func:
        gens.append(gen_deri_factor)
    factor = random.choice(gens)(max_length, max_cost)
    return factor


def gen_deri_factor(max_length, max_cost):
    deri_factor = DeriFactor()
    length = 4
    expr = gen_expr(max_length - length, int(math.log2(max_cost)))
    length += expr.len
    deri_factor.expr = expr
    deri_factor.to_string()
    return deri_factor


def gen_exp_factor(max_length, max_cost):
    exp_factor = ExpFactor()
    length = 5
    factor = gen_factor(max_length - length, max_cost - 1)
    length += factor.len
    exp_factor.factor = factor
    if is_strong:
        max_cost = exp_factor.get_cost() + 100
    if max_length - length > 2 and exp_factor.get_cost() < max_cost:
        length += 1
        number = gen_index(int(math.log2(max_cost - exp_factor.get_cost())))
        exp_factor.index = number
        length += number.len
    exp_factor.to_string()
    return exp_factor


def gen_func_factor(max_length, max_cost):
    func_factor = FuncFactor()
    length = 3
    func_factor.function = random.choice(functions)
    var_num = func_factor.function.var_num
    for i in range(0, var_num):
        cost = max_cost * 2
        var_max_cost = 500
        while cost > max_cost:
            factor = gen_factor(random.randint(1, max_length - length - var_num + i + 1), var_max_cost)
            func_factor.var_list[i] = factor
            func_factor.to_string()
            cost = func_factor.get_cost()
            var_max_cost >>= 1
            if is_strong:
                cost = max_cost
        length += factor.len
    func_factor.to_string()
    return func_factor


def gen_var_factor(max_length, max_cost):
    var_factor = VarFactor()
    if is_func > 0:
        var_factor.name = random.choice(var_lists[0:is_func])
    length = 1
    if is_strong:
        max_cost = var_factor.get_cost() + 100
    if max_length - length > 2 and var_factor.get_cost() < max_cost:
        length += 1
        number = gen_index(8)
        var_factor.index = number
        length += number.len
    var_factor.to_string()
    return var_factor


def gen_con_factor(max_length, max_cost):
    con_factor = ConFactor()
    length = 1
    con_factor.is_negative = random.choice([False, True])
    number = gen_number(random.randint(1, max_length - length),
                        max_cost - 1)
    length += number.len
    con_factor.number = number
    con_factor.to_string()
    return con_factor


def gen_expr_factor(max_length, max_cost):
    expr_factor = ExprFactor()
    length = 1
    expr = gen_expr(random.randint(3, max_length - 2), max_cost - 1)
    length += expr.len + 1
    expr_factor.expr = expr
    if is_strong:
        max_cost = expr_factor.get_cost() + 100
    if max_length - length > 2 and expr_factor.get_cost() < max_cost:
        length += 1
        number = gen_index(int(math.log(max_cost) / math.log(expr_factor.get_cost())))
        expr_factor.index = number
        length += number.len
    expr_factor.to_string()
    return expr_factor


def gen_number(max_length, max_cost):
    number = Number()
    lens = random.randint(1, min(max_length, min(max_cost, 10)))
    for i in range(0, lens):
        number.number += str(random.randint(0, 9))
    number.to_string()
    return number


def gen_index(max_cost):
    number = Number()
    minn = 0
    maxx = min(8, max_cost)
    number.number += str(random.randint(minn, maxx))
    number.to_string()
    return number
