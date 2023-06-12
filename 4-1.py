q=input().split()

i=0
answer=[]
while i <len(q):
  answer.append(q[i][::-1])
  i+=1
print(" ".join(answer))

