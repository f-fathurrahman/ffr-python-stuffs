
import subprocess
import sys
import os

# set GKW_WSTYPE, we will save the output to a file
os.environ["GKS_WSTYPE"] = "mov"

Nargs = len(sys.argv)
if Nargs <= 2:
    raise RuntimeError("Nargs must be >= 2")

fileout = sys.argv[2]

p = subprocess.Popen("python " + sys.argv[1], shell=True)
(output, err) = p.communicate() 
p_status = p.wait()

os.rename("gks.mov", fileout)

