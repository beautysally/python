a=input().split()
t=['星期五','星期六','星期日']
x=a[0]
y=int(a[1])
z=int(a[2])
if x in t:
  print('不開市')
else:
  print(y*z)

