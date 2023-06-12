a=input()
if'+' in a:
  x=a.split('+')
  print(int(x[0])+int(x[1]))
elif'-' in a:
  x=a.split('-')
  print(int(x[0])-int(x[1]))
elif'*' in a:
  x=a.split('*')
  print(int(x[0])*int(x[1]))
else:
  x=a.split('/')
  print(int(x[0])/int(x[1]))