import subprocess, os

dir = os.getcwd()
subprocess.run(['git'], ['status'], cwd=dir)