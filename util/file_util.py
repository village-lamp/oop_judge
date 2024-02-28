def read(path):
    file = open(path, "r")
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
