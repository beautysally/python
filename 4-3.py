a=int(input())
min=0
nums=[]
for a in range(min,a+1):
  if a>1:
    for i in range(2,a):
      if(a%i)==0:
       break
    else:
      nums.append(a)
print(max(nums))