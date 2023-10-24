"""
情报加密 - 《Python编程基础及应用》习题6-10
【问题描述】
某情报机构采用公用电话传递数据，数据是5位的整数，在传递过程中是加密的。加密规则如下：每位数字都加上8,然后用和除以7的余数代替该数字，再将第1位和第5位交换，第2位和第3位交换。请编写程序，完成明文至密文的加密过程。
【输入形式】
符合题目要求的5位整数
【输出形式】
加密后的密文整数
【样例输入】
12345
【样例输出】
64352
"""


def encrypt(num):
    # 转换数字为字符串
    num_str = str(num)

    # 对每一位数字都加8，并求与7的余数
    encrypted_str = ''.join([str((int(digit) + 8) % 7) for digit in num_str])

    # 将第1位和第5位交换，第2位和第3位交换
    encrypted_str = encrypted_str[4] + encrypted_str[2] + encrypted_str[1] + encrypted_str[3] + encrypted_str[0]

    return int(encrypted_str)


def main():
    num = int(input())
    print(encrypt(num))


# 调用主函数
if __name__ == "__main__":
    main()
