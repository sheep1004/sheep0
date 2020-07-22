"""
输出100以内所有的素数。

说明：素数指的是只能被1和自身整除的正整数（不包括1）
"""
from math import sqrt

for i in range(2,100):
    end = int(sqrt(i))
    flag = 0
    for j in range(2,end+1):
        if i%j == 0:
            flag=1
            break
    if flag == 0:
        print(i)
