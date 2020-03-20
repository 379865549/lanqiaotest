n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
for i in range(n):
    print(list1[i],end=' ')