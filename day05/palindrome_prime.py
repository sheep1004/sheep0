"""
写一个程序判断输入的正整数是不是回文素数
"""
import day05.prime_num as prime
import day05.parlindrome_number as par

if __name__ == '__main__':
    num = int(input('请输入数字：'))
    flag_par = par.is_palindrome(num)
    flag_pri = prime.prime(num)
    if 1 == flag_pri and flag_par:
        print("该数是回文素数！")
    else:
        print('该数不是回文素数！')