"""
生成斐波那契数列的前20个数
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
"""
a = 1
b = 1
sum = 0
print(a)
print(b)
for i in range(1,21):
    sum = a + b
    a = b
    b = sum
    print(sum)
