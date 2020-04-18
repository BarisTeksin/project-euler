num = 3
prime = 1
while True:
    check = True
    if num % 2 != 0 or num % 5 != 0:
        for x in range(2,num):
            if num % x == 0:
                check = False
                break
        if check:
            prime += 1
            if prime == 10001:
                break
    num += 1 
print(num)
