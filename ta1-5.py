id=input()
ck = 0
if id[0] == 'A':
  ck += 1+0*9
elif id[0] == 'B':
  ck += 1+1*9
elif id[0] == 'C':
  ck += 1+2*9
elif id[0] == 'D':
  ck += 1+3*9
elif id[0] == 'E':
  ck += 1+4*9
elif id[0] == 'F':
  ck += 1+5*9
elif id[0] == 'G':
  ck += 1+6*9
elif id[0] == 'H':
  ck += 1+7*9
elif id[0] == 'I':
  ck += 3+4*9
elif id[0] == 'J':
  ck += 1+8*9
elif id[0] == 'K':
  ck += 1+9*9
elif id[0] == 'L':
  ck += 2+0*9
elif id[0] == 'M':
  ck += 2+1*9
elif id[0] == 'N':
  ck += 2+2*9
elif id[0] == 'O':
  ck += 3+5*9
elif id[0] == 'P':
  ck += 2+3*9
elif id[0] == 'Q':
  ck += 2+4*9
elif id[0] == 'R':
  ck += 2+5*9
elif id[0] == 'S':
  ck += 2+6*9
elif id[0] == 'T':
  ck += 2+7*9
elif id[0] == 'U':
  ck += 2+8*9
elif id[0] == 'V':
  ck += 2+9*9
elif id[0] == 'W':
  ck += 3+2*9
elif id[0] == 'X':
  ck += 3+0*9
elif id[0] == 'Y':
  ck += 3+1*9
else:
  ck += 3+3*9
ck += int(id[1])*8
ck += int(id[2])*7
ck += int(id[3])*6
ck += int(id[4])*5
ck += int(id[5])*4
ck += int(id[6])*3
ck += int(id[7])*2
ck += int(id[8])
ck += int(id[9])
if ck% 10 == 0:
  print('合法')
else:
  print('不合法')