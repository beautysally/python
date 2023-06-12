# q=list(map(int, input().split()))
# i=0
# answer=" " 
# while i <len(q):
#   answer+=str(int(q[i])+1)+" "
#   i+=1
# print(answer)

#-----------------
# q=input().split()

# answer=[]
# for s in q:
#   answer.append(str(int(s)+1))

#   print(' '.join(answer))
 
#-----------------
print(' '.join([str(int(s)+1)for s in input().split()]))
