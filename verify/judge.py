import os
import re
import shutil
import zipfile

import sympy

from generate.exprs.expr import Expr
from generate.generator import gen_null
from util.file_util import write, read
from util.java_util import process_java


class Judge:

    def __init__(self, path, zip_name):
        self.path = path
        self.base_path = os.path.join(path, "source_code")
        self.target_path = os.path.join(path, "target")
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

    def clear(self):
        shutil.rmtree(self.base_path)
        os.mkdir(self.base_path)
        shutil.rmtree(self.target_path)
        os.mkdir(self.target_path)

    def judge(self, inputs: list, null_times):
        self.unzip()

        ret = []
        out, main_path, main_name = process_java(self.base_path, self.target_path)
        if main_name == "":
            out = "未找到main"
        if out is not None:
            self.clear()
            return ["编译错误", out]
        else:
            ret.append("编译成功")

        for i in range(0, len(inputs)):
            input_path = os.path.join(self.test_path, "input{0}.txt".format(i + 1))
            output_path = os.path.join(self.test_path, "output{0}.txt".format(i + 1))
            # write(input_path, gen_null(inputs[i], null_times))
            write_inputs = []
            for strs in inputs[i]:
                if type(strs) is Expr:
                    write_inputs.append(strs.str)
                else:
                    write_inputs.append(str(strs))
            write(input_path, write_inputs)
            print("write input\n")
            os.system("copy {0} {1}".format(input_path,
                                            os.path.join(self.target_path, "input.txt")))
            os.system("java -jar {0} {1} {2}".format(os.path.join(self.target_path, "project.jar"),
                                                     os.path.join(self.target_path, "input.txt"),
                                                     os.path.join(self.target_path, "output.txt")))
            out = read(os.path.join(self.target_path, "output.txt"))
            print("run finished\n")
            if out.find("Exception") != -1:
                inputs_str = ""
                for j in range(0, len(inputs[i]) - 1):
                    inputs_str = str(inputs[i][j]) + '\n'
                inputs_str += inputs[i][len(inputs[i]) - 1].str
                ret.append(["运行错误", out, inputs_str])
                continue
            os.system("copy {0} {1}".format(os.path.join(self.target_path, "output.txt"),
                                            output_path))
            ver = self.verify(out, inputs[i][len(inputs[i]) - 1].sympy_str)
            if ver[0] == "答案错误":
                ver.append(read(input_path))
            ret.append(ver)

        self.clear()
        return ret

    def verify(self, out, stdout):
        out = out.replace("^", "**")
        stdout = stdout.replace("^", "**")
        stdout = sympy.expand(stdout)
        if not self.is_legal(out):
            return ["答案错误", out, stdout]
        try:
            v_out = sympy.expand(out)
        except:
            print("exception")
            return ["答案错误", out, stdout]
        if v_out == stdout:
            return ["答案正确"]
        else:
            return ["答案错误", out, stdout]

    def is_legal(self, out: str):
        pos = 0
        left_pos = out.find("(", pos)
        # 找到exp以及括号，比较位置是否相同，如果不同说明有不必要的括号
        while left_pos != -1:
            pos = out.find("exp", pos)
            if pos + 3 != left_pos:
                return False

            # 找到右括号位置
            right_pos = self.get_right_brace(out, left_pos)
            pos = right_pos + 1

            inner = out[left_pos + 1:right_pos]
            if out[left_pos + 1] == "(" and out[right_pos - 1] == ")":
                if self.is_legal(out[left_pos + 2:right_pos - 1]):
                    left_pos = out.find("(", pos)
                    continue
                else:
                    return False

            if re.fullmatch("x(\\*\\*\\+?\\d+)?", inner) is not None:
                left_pos = out.find("(", pos)
                continue

            if re.fullmatch("[+-]?\\d+", inner) is not None:
                left_pos = out.find("(", pos)
                continue

            if inner[0:3] == "exp":
                right_pos = self.get_right_brace(inner, 3)
                rest = inner[right_pos + 1:]
                if re.fullmatch("(\\*\\*\\+?\\d+)?", rest) is not None:
                    left_pos = out.find("(", pos)
                    continue

            return False

        return True


    def get_right_brace(self, strs, left_pos):
        bra = 1
        right_pos = left_pos + 1
        while bra > 0:
            if strs[right_pos] == "(":
                bra += 1
            if strs[right_pos] == ")":
                bra -= 1
            right_pos += 1
        return right_pos - 1
