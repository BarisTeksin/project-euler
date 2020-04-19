n = 2000000
sum, temp = 0, [True] * n
for p in range(2, n):
    if temp[p]:
        sum += p
        for i in range(p*p, n, p):
            temp[i] = False

print(sum)
