from itertools import product
alph = 'САШУЛЯ'
k = 0
for x in product(alph, repeat=7):
    s = "".join(x)
    if s.count("С") == 1 and s.count("Я") == 1 and s[0] != "Я":
        k += 1
print(k)