a=int(input())
if (a%4)==0 and (a%100)!=0:
  print('a leap year')
elif(a%400)==0:
  print('a leap year')
else:
  print('a normal year')


