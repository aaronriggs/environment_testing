# testing subprocess to run commands on macos
import subprocess
try:
    cmd = subprocess.run(["brew", "update"])
    print(cmd)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
