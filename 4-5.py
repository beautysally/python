a=int(input())
count=0
while a:
  if a%2:
    a-=1
  else:
    a/=2
  count+=1
print(count)
