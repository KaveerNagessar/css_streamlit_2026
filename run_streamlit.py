
import subprocess

file = "app-Copy5.py"

subprocess.Popen(
    ["streamlit", "run", file], shell=True
)