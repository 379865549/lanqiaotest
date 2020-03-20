for i in range(32):
    a =  str(bin(i))
    b = a[2:]
    c = '00000'
    d = c[:5-len(b)] + b
    print(d)
