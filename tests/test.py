import glob, os

for file in os.listdir("tests/"):
    if file.endswith(".yml") and file.startswith("playbook"):
        os.system(f"ansible2puml --source tests/{file} --destination temp.puml")