a = str(input()).lstrip("0")
b = str(input()).lstrip("0")
if not len(a):
    a = "0"
if not len(b):
    b = "0"
c = ""
ostat = 0
for i in range(-1, -max(len(a), len(b)) - 1, -1):
    if abs(i) <= len(a) and abs(i) <= len(b):
        summa = int(a[i]) + int(b[i]) + ostat
        c = str(summa % 10) + c
        ostat = summa // 10
    elif abs(i) <= len(a):
        c = str(int(a[i]) + ostat) + c
        ostat = 0
    elif abs(i) <= len(b):
        c = str(int(b[i]) + ostat) + c
        ostat = 0

print(c)
