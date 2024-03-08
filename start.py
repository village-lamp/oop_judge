import os

import generate.generator
from verify.judge import Judge

test_data = [[20, 10, 500, 200], [50, 20, 5000, 2000], [200, 150, 50000, 2000]]


def start(user_name, zip_name, times, test_type):
    tests = []
    for i in range(0, int(times)):
        inputs = generate.generator.gen_test(test_data[test_type][0],
                                             test_data[test_type][1],
                                             test_data[test_type][2],
                                             test_data[test_type][3])
        tests.append(inputs)
    judge = Judge(os.path.join("resources", user_name), zip_name)
    return judge.judge(tests, 0)
