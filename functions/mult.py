import sys

def hcf(x, y):

    while(y):
        x, y = y, x % y

    return x

a,b = map(int,sys.stdin.readline().split())

res=int(((a*b)/hcf(a,b)))
print(res)
