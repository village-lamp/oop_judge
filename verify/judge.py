import os
import shutil
import zipfile

import jpype
import sympy

from generate.generator import gen_null
from util.file_util import write, read
from util.java_util import compile_java


def init():
    jpype.startJVM(jpype.getDefaultJVMPath())


class Judge:

    def __init__(self, path, zip_name):
        self.path = path
        self.base_path = os.path.join(path, "source_code")
        self.target_path = os.path.join(path, "target")
        jpype.addClassPath("..\\" + self.target_path)
        self.test_path = os.path.join(path, "test")
        self.zip_path = os.path.join(self.base_path, zip_name)

    def diverse_file(self, path):
        for file_name in os.listdir(path):
            full_path = os.path.join(path, file_name)
            if os.path.isfile(full_path):
                if file_name == "Main.class":
                    return path
            else:
                self.diverse_file(full_path)
        return ""

    def unzip(self):
        with zipfile.ZipFile(self.zip_path, "r") as zf:
            file_list = zf.namelist()
            for file in file_list:
                zf.extract(file, path=self.base_path)

    def judge(self, inputs: list, null_times):
        self.unzip()

        out = compile_java(self.base_path, self.target_path)
        main_path = self.diverse_file(self.target_path)
        if main_path == "":
            print("未找到Main.java\n")
            return
        start_class = jpype.JClass("Start")
        start = start_class()
        if out is not None:
            print("编译错误：\n" + out)
            return
        else:
            print("编译成功：\n")

        for i in range(0, len(inputs)):
            input_path = os.path.join(self.test_path, "input{0}.txt".format(i + 1))
            write(input_path, gen_null(inputs[i].to_string(), null_times))
            os.system("copy {0} {1}".format(input_path,
                                            os.path.join(main_path, "input.txt")))
            try:
                start.main([os.path.join(main_path, "input.txt"),
                            os.path.join(main_path, "output.txt")])
            except Exception as e:
                print("Runtime Error:\n" + str(e))
                return
            out = read(os.path.join(main_path, "output.txt"))
            print(self.verify(out, inputs[i].to_string(True)))

        shutil.rmtree(self.target_path)
        os.mkdir(self.target_path)
        shutil.rmtree(self.base_path)
        os.mkdir(self.base_path)

    def verify(self, out, stdout):
        out.replace("^", "**")
        stdout.replace("^", "**")
        stdout = sympy.expand(stdout)
        try:
            v_out = sympy.expand(out)
        except:
            print("")
            return "输出格式错误, 输出:" + out + " 参考输出:" + str(stdout) + "\n"
        if v_out == stdout:
            return "答案正确\n"
        else:
            return "答案错误, 输出:" + out + " 参考输出:" + str(stdout) + "\n"
