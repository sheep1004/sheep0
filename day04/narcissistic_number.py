"""
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$
"""
for a in range(100,1000):
    ud = a%10   #unit's digit 个位
    td = a//10%10   #ten's digit 十位
    hd = a//100    #hundred's digit 百位
    if a== ud**3 + td**3 + hd**3:
        print(a)