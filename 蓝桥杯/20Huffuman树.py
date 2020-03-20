n=int(input())
if  0<=n<=100:
    list1=list(map(int,input().split()))
    list1.sort(reverse=True)
    while list1[0]>1000:
        del(list1[0])#进行删除
    total=0
    while len(list1)>1:
        list1.sort(reverse=True)
        num=list1.pop()+list1.pop()
        total=total+num
        list1.append(num)
    print(total)

