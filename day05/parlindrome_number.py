"""
实现判断一个数是不是回文数的函数
"""
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    #total记录temp中的数反转后的值（day04 reverse),两者比较获得结果
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num