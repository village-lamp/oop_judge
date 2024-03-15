import os

import generate.generator
from util.file_util import read_list
from verify.judge import Judge

test_data = [[20, 10, 500, 200, False], [50, 20, 5000, 2000, False], [200, 150, 500000, 20000, False]]


def start(user_name, zip_name, times, test_type):
    tests = []
    if test_type <= 2:
        for i in range(0, int(times)):
            inputs = generate.generator.gen_test(test_data[test_type][0],
                                                 test_data[test_type][1],
                                                 test_data[test_type][2],
                                                 test_data[test_type][3],
                                                 test_data[test_type][4])
            tests.append(inputs)
    else:
        path = "resources\\common\\test"
        i = 1
        file_path = os.path.join(path, "input1.txt")
        while os.path.exists(file_path):
            tests.append(read_list(file_path))
            i += 1
            file_path = os.path.join(path, f"input{i}.txt")
    judge = Judge(os.path.join("resources", user_name), zip_name)
    return judge.judge(tests, 0)
