""" def triangles():
    p = [1]
    while True:
        yield p#generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break """
""" def triangles():
    a = [1] 
    while True: 
        yield a 
        a = [sum(i) for i in zip([0] + a, a + [0])] """

t = int(input())
print (1)
line = [1,1]
line1 = ['1','1']
print(' '.join(line1))
for i in range(2,t):
	r = []
	for i in range(0,len(line)-1):
		r.append(line[i]+line[i+1])
	line = [1]+r+[1]
	c = map(str,line)
	print(' '.join(c))

