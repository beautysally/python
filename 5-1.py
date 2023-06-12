a=input()
a_dict={}
for i in range(len(a)-1,-1,-1):
  if a[i] not in a_dict:
    a_dict[a[i]]=i
sort_dict=sorted(a_dict.values())
ans=''.join([a[i]for i in sort_dict])
print(ans)