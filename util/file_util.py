import os.path


def read(path):
    file = open(path, "r", encoding="utf-8")
    content = str(file.read())
    file.close()
    return content


def write(path, inputs):
    file = open(path, "w")
    if type(inputs) is str:
        file.write(inputs)
    else:
        if type(inputs) is list:
            for strs in inputs:
                file.write(strs)
                file.write("\n")

    file.close()


def read_list(path):
    content = read(path)
    return content.split("\n")


def add_test(inputs):
    inputs = inputs.split("\n")
    inputs.remove("")
    path = "resources\\common\\test"
    i = 1
    while os.path.exists(os.path.join(path, f"input{i}.txt")):
        i += 1
    write(os.path.join(path, f"input{i}.txt"), inputs)
