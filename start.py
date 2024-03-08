import os

import generate.generator
from verify.judge import Judge


def start(user_name, zip_name, times, max_length):
    tests = []
    for i in range(0, int(times)):
        inputs = generate.generator.gen_test(max_length)
        tests.append(inputs)
    judge = Judge(os.path.join("resources", user_name), zip_name)
    return judge.judge(tests, int(max_length / 5))
