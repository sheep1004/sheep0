"""
输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数.
"""
a = int(input('a='))
b = int(input('b='))
if a > b:
    a,b = b,a
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        GCD = i
        break
LCM = a*b//GCD #最小公倍数=两数相乘/最大公约数 ,由于除法有小数位，使用int返回会出错，故使用整除
print(f'最大公因数为：{GCD:d}')
print(LCM)