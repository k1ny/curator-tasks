a = 2*22**3 + 3 * 22**2 + 5
b = 6 * 13**4 + 7 * 13**3 + 9 * 13

for x in range(0,22):
    for y in range(0,13):
        s = a + b + x * 22 + x * 22 ** 4 + y + y * 13 ** 2
        if s%57 == 0:
            print(s//57, x+y)