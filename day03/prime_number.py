"""
输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。
算法改进：一个数若可以进行因数分解，那么分解时得到的两个数一定是一个小于等于sqrt(n)，一个大于等于sqrt(n)，据此，上述代码中并不需要遍历到n-1，遍历到sqrt(n)即可，因为若sqrt(n)左侧找不到约数，那么右侧也一定找不到约数。
"""
from math import sqrt

num = int(input('请输入数字：'))
end = int(sqrt(num))
flag = 0
if num <= 1:
    print("素数为大于1的正整数，请重新输入：")
else:
    for i in (2,end+1):
        if num%i == 0:
            flag=1
            break
    if flag == 1:
        print('%d不是素数' % num)
    else:
        print('%d是素数'%num)