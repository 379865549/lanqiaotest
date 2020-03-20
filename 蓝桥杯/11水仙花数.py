for i in range(100,1000):
    a = i % 10
    b = int((i / 10) % 10)
    c = int(i / 100)
    if (a**3+b**3+c**3) == i:
        print(i)
    