from generate.generator import gen_test

lists = gen_test(200, 150, 5000, 2000, True)
for strs in lists:
    print(strs)
