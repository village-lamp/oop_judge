import os

import generate.generator
from verify.judge import Judge, init


# def start(user):
init()
n = int(input("输入测试次数："))
max_length = int(input("输入长度上限："))
tests = []
for i in range(0, n):
    expr, _ = generate.generator.gen_expr(max_length)
    tests.append(expr)
judge = Judge(os.path.join("resources", "admin"), "1.zip")
judge.judge(tests, int(max_length / 10))
