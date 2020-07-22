"""
实现判断一个数是不是素数的函数。
"""
from math import sqrt

#是素数返回1，不是素数返回0
def prime(num):
    end = int(sqrt(num))
    flag = 0
    for i in (2, end + 1):
        if num % i == 0:
            flag = 1
            break
        if flag == 1:
            return 0
        else:
            return 1


if __name__ == '__main__':
    num = int(input('请输入数字：'))
    if num <= 1:
        print("素数为大于1的正整数，请重新输入：")
    else:
        f = prime(num)
        if f ==1:
            print("该数是素数")
        else:
            print("该数不是素数")