import os
import subprocess
import re

from util import file_util
from util.file_util import read, write

file_list = []
main_path = ""
main_name = ""
start_path = "resources\\common\\Start.java"


def process_java(code_path, target_path):
    out = compile_java(code_path, target_path)
    pack_java(target_path)
    return out, main_path, main_name


def compile_java(code_path, target_path):
    global file_list, main_path, main_name
    file_list = []

    main_path = ""
    main_name = ""
    diverse_file(code_path)
    copy_start()

    file_util.write(os.path.join(code_path, "javaList.txt"), file_list)
    cmd = "javac @{0} -encoding UTF-8 -d {1}".format(os.path.join(code_path, "javaList.txt"),
                                                     target_path)
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.wait()
    out = process.stdout.read()

    if out == "":
        return None
    return out


def copy_start():
    strs = read(start_path)
    strs.replace("Main", main_name)
    write(os.path.join(main_path, "Start.java"), strs)
    file_list.append(os.path.join(main_path, "Start.java"))


def pack_java(target_path):
    write(os.path.join(target_path, "Manifest.txt"),
          "Main-Class: Start\n")
    os.chdir(target_path)
    os.system("jar cfm project.jar Manifest.txt .")
    os.chdir("../../..")


def diverse_file(path):
    global main_path, main_name
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
            diverse_file(full_path)
