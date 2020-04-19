def pythagorean(num):
    for c in range(2,num):
        for b in range(2,num):
            for a in range(2,num-c-b+1):
                if a + b + c == num and c > b and c > a and (b > a or a > b) and a**2 + b**2 == c**2:
                    print('A : ' + str(a) + ' B : ' + str(b) + ' C : ' + str(c) + ' SONUÇ : ' + str(a*b*c))
                    return a*b*c

print(pythagorean(1000))
