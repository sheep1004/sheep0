"""
打印三角形图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""
n = int(input('请输入需要打印的行数：'))
#第一个三角形
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*', end='') #python中print打印自动换行
    print()#换行
print()#空行
#第二个三角形
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ", end='')
    for k in range(1,i+1):
        print('*', end='')
    print() # 换行
#print('\n')#空2行
print() # 换行
#第三个三角形
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ", end='')
    for j in range(1,2*i):
        print('*', end='')
    print()# 换行
print()  # 空行
