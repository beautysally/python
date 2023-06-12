x,y=map(int,input().split())
x=int(x)
y=int(y)
i=1
while i<=x:
  k=1
  while k<=y:
    print(f'{i}x{k}={i*k}')
    k+=1
  i+=1

 