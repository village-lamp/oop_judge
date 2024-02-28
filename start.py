import os

import generate.generator
from verify.judge import Judge


def start(user_name, zip_name, times):
    max_length = 50
    tests = []
    for i in range(0, int(times)):
        expr, _ = generate.generator.gen_expr(max_length)
        tests.append(expr)
    judge = Judge(os.path.join("resources", user_name), zip_name)
    return judge.judge(tests, int(max_length / 10))
