import subprocess

# result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
# >>> result.stdout

for i in range(1,114+1):
    str_surat = "%03d" % i
    lst_str = subprocess.check_output(["ls", "-l", str_surat]).decode().split("\n")
    Nayat = len(lst_str) - 3
    print("%d : %d," % (i,Nayat))
