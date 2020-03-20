n = int(input())
list1 = list(map(int,input().split()))
m = int(input())
if m in list1:
    print(list1.index(m)+1)
else:
    print(-1)