from generate.generator import gen_test

for i in range(0, 20):
    lists = gen_test(200, 150, 5000, 2000, True)
    for strs in lists:
        print(strs)
