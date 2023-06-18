import os
import subprocess

# run a shell script from a python script

# stores the file path to the current file
script_dir = os.path.dirname(__file__)

# stores the file path to the script you want to run
script_absolute_path = os.path.join(script_dir + "/shell_script.sh")

# calls the shell file and runs it
subprocess.call(['sh', script_absolute_path])