import os
import subprocess
import re

from util import file_util
from util.file_util import read, write

file_list = []
start_path = "resources\\common\\Start.java"


def compile_java(base_path, target_path):
    global file_list
    file_list = []

    main_path, main_name = diverse_file(base_path)
    copy_start(main_path, main_name)

    # os.system("copy {0} {1}".format(start_path, os.path.join(path, "Start.java")))
    # file_list.append(os.path.join(path, "Start.java"))

    file_util.write(os.path.join(base_path, "javaList.txt"), file_list)
    cmd = "javac @{0} -encoding UTF-8 -d {1}".format(os.path.join(base_path, "javaList.txt"),
                                                     target_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()
    out = process.stdout.read()

    if out == "":
        return None, main_path, main_name
    return out, main_path, main_name


def copy_start(main_path, main_name):
    strs = read(start_path)
    strs.replace("Main", main_name)
    write(os.path.join(main_path, "Start.java"), strs)
    file_list.append(os.path.join(main_path, "Start.java"))


def diverse_file(path):
    main_path = ""
    main_name = ""
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        if os.path.isfile(full_path):
            if not re.match(".*\\.java", file_name):
                continue
            file_list.append(full_path)
            strs = read(full_path)
            if strs.find("public static void main") != -1:
                main_path = path
                main_name = file_name
        else:
            main_path, main_name = diverse_file(full_path)
    return main_path, main_name
