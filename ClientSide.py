import subprocess
import gc
prf = ["env", "DISPLAY=:0",   "XAUTHORITY=/home/ourname/.Xauthority"]
while True:
    r1 = subprocess.run(['xhost', 'local:root'],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL )
    r2 = subprocess.run([prf[0], prf[1], prf[2],"wmctrl", "-l", "-p", "-lp"],  encoding='utf-8', stdout=subprocess.PIPE)
    print(r2)
    if r1.returncode == 0 and r1.returncode == 0:
        print("List  of open Applications  ")
        break
r1 = subprocess.run([prf[0], prf[1], prf[2],"wmctrl", "-l", "-p","-lp"],  encoding='utf-8', stdout=subprocess.PIPE)
for line in r1.stdout.split('\n'):
    print(line)
    gc.collect()
  