def fib(n):
    x = [0, 1]
    while x[-1]+x[-2] <= n:
         x.append(x[-1]+x[-2])
    return x
print(sum(n for n in fib(4000000) if n%2==0))
