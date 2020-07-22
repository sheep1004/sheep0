"""
正整数的反转

Version: 0.1
Author: 骆昊
"""

num = int(input('num = '))
reversed_num = 0
while num > 0:
    #每次取原数最后一位至末尾，组成新数，原数整除10，准备下一次循环
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
