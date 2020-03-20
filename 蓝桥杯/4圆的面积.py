def yuan(r):
    PI=3.14159265358979323
    sear =  PI * r ** 2 
    return "{:.7f}".format(sear)
r = int(input())
print(yuan(r))