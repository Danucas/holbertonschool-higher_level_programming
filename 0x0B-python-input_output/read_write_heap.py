#!/usr/bin/python3

import os
import subprocess

process = subprocess.run(["ps", "m"], stdout=subprocess.PIPE)
result = str(process.stdout).split('\\n')
line_n = 0
for i, line in enumerate(result):
    if "printer.py" in line:
        line_n = i
        print("\033[32m", end='')
    print(line, "\033[0m")
pid = result[line_n][:5].strip()

print("\033[36m" + pid + "\033[0m")
