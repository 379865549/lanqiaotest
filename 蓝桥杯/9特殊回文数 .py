n = int(input())
for i in range(10000,1000000):
    A = str(i)
    B = int(A[::-1])
    if B == i:
        C = int((str(i))[0:3])
        a = int(C/100)
        b = int((C/10)%10)
        c = int(C%10)
        if i<=100000:
            if ((a+b)*2)+c == n:
                print(i)
        else:
            if (a+b+c)*2 == n:
                print(i)
