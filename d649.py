# while True:
#     a = int(input())
#     if a != 0:
#         for i in range(1, a + 1):
#             print("_" * (a - i) + "+" * i)
#         continue
#     else:
#         break

a=int(input())
if a!=0:
    for i in range(1,a+1):
        print(i)
        print("_" * (a - i) + "+" * i)