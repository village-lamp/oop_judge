from generate.generator import gen_test

lists = gen_test(50, 20, 5000, 2000, False)
for strs in lists:
    print(strs)
