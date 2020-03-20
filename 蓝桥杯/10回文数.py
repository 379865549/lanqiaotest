for i in range(1000,10000):
    A = str(i)
    B = int(A[::-1])
    if B == i:
        print(i)
