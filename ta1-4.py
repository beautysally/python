x= input().split(",") #輸入資料根據","使用split分開

a= x[0].split() #根據空白使用split切開,設定第一個變數
b= x[1].split() #根據空白使用split切開,設定第二個變數
count =0 #設定一個計算變數,以利後續判斷對中幾個數字,初始值為0
if a[0] in b: #判斷第一個變數的第一個值,是否在第二個變數內
  count+=1 #把計數變數+1
if a[1] in b:
  count+=1
if a[2] in b:
  count+=1
if a[3] in b:
  count+=1
if a[4] in b:
  count+=1
if count<3:
  print("0")
elif count == 3:
  print("100")
elif count == 4:
  print("1000")
else:
  print("10000")