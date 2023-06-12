rob=input()
x=0
y=0
for robs in rob:
  if robs =="U":
    y+=1
  elif robs =="D":
    y-=1
  elif robs =="L":
    x-=1
  elif robs =="R":
    x+=1
if x==0 and y==0:
  print("Y")
else:
  print("N")

  # rob= input()
# l=len(rob)
# X=0
# Y=0
# for r in range(0,l):
#   if rob[r] == "U": 
#     Y += 1
#   elif rob[r] == "D":
#     Y -= 1
#   elif rob[r] == "L":
#     X -= 1
#   elif rob[r]== "R":
#     X +=1
# if X==0 and Y==0:
#   print("Y")
# else:
#   print("N")
