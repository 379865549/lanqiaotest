try:
    n, m = map(int, input().split())
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = letter[:m]
    for i in range(1, n + 1):
        print(x)
        x = letter[i] + x[0:-1]
except:
   pass