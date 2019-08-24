import subprocess

run_args = ['python', 'thenHere.py']
process = subprocess.Popen(run_args)
process.wait()
