import os.path

from util.java_util import process_java

os.chdir("..")
base_path = "resources\\3f39f875a501422aded24cccae49cc9b21eba8283275b8eaa94bd70d3d262ce9"
target_path = os.path.join(base_path, "target")
code_path = os.path.join(base_path, "source_code")

process_java(code_path, target_path)
