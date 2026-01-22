def nf(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f

print(nf(10))

print('exemplo utilizando for')

for i in range(5): print(nf(i))