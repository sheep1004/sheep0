"""
实现计算求最大公约数和最小公倍数的函数
"""
def GCD(a,b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
           return i

def LCM(gcd):
    c = a*b//GCD
    return c

a = int(input('a='))
b = int(input('b='))
if a > b:
    a,b = b,a
GCD = GCD(a,b)
LCM = LCM(GCD)  #最小公倍数=两数相乘/最大公约数 ,由于除法有小数位，使用int返回会出错，故使用整除
print(f'最大公约数为：{GCD:d}')
print(f'最小公倍数为{LCM:d}')