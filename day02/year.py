"""
输入年份判断是不是闰年
符合下面两个条件之一的年份是闰年:
（1） 能被4整除但不能被100整除。 （2） 能被400整除。
"""
a = int(input('请输入年份：'))
if a%4==0 and a % 100 != 0 or a%400 ==0:
    print(f'{a:d}是闰年')
else:
    print(f'{a:d}不是闰年')