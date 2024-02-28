import os
import subprocess
import re

from util import file_util

file_list = []


def compile_java(base_path, target_path):
    global file_list
    file_list = []
    diverse_file(base_path)
    file_util.write(os.path.join(base_path, "javaList.txt"), file_list)
    cmd = "javac @{0} -encoding UTF-8 -d {1}".format(os.path.join(base_path, "javaList.txt"),
                                                     target_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()
    out = process.stdout.read()

    if out == "":
        return None
    return out


def diverse_file(path):
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        if os.path.isfile(full_path):
            if not re.match(".*\\.java", file_name):
                continue
            file_list.append(full_path)
            if file_name == "Main.java":
                os.system("copy resources\\common\\Start.java {0}".format(os.path.join(path, "Start.java")))
                file_list.append(os.path.join(path, "Start.java"))
        else:
            diverse_file(full_path)
    return True
