with open('k8-0.txt') as f:
    s = f.readline()

k = 1
mas = [0]*(ord("Z") - ord("0") + 1)

for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        k += 1
        index = ord(s[i]) - ord("0")
        mas[index] = max(mas[index], k)
    else:
        k = 1

for i, cnt in enumerate(mas, ord("0")):
    if cnt == max(mas):
        print(chr(i), cnt, end=" ")
