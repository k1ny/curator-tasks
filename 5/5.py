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

for i in range(len(mas)):
    if mas[i] == max(mas):
        print(chr(i + ord("0")), mas[i], end=" ")
