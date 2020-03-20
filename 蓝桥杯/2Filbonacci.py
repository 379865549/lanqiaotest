def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
        a = a%10007
    return a
n = int(input())
print(fib(n))