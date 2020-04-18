num = 1
while True:
    result = True
    if num % 2 !=0 or num % 5 != 0:
        num += 1
        continue
    for x in range(1,21):
        if num % x != 0:
            result = False
            break
    if result:
        break
    else:
        num += 1
print(num)
