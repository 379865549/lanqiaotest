n = int(input())
result = []
for i in range(n):
    a = int(input(),16)
    b = str(oct(a))
    c = int(b[2:])
    result.append(c)
for i in range(n):
    print(result[i])