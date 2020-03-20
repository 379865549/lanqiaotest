n = int(input())
flag = n % 2
b = n // 2
if flag:
    a = (1 + n)/2 * n
else:
    a = (1 + n) * b
print(int(a))

