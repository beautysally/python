# 2
# 1 2 3 4
# 1 2 4 8

n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if(b-a)==(c-b)==(d-c):
        print(a,b,c,d,d+(d-c))
    else:
        print(a,b,c,d,d*(d//c))