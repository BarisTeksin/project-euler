d = 600851475143
x = 2
while x <= d-1:
    if d%x==0:
        d=d/x
    x=x+1
print(x)
