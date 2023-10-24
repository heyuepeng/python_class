"""
分数化简
【问题描述】
编写程序，从控制台读入一个分数的分子和分母（分数无符号，并且分子小于分母，其大小不会超过int数据类型的表示范围），输出化简后分子和分母不含公约数的分数。
【输入形式】
从控制台输入两个正整数分别表示分子和分母，两整数之间以一个空格分隔。
【输出形式】
在标准输出上输出化简后的分子和分母，以一个空格分隔。
【输入样例1】
26664 479952
【输出样例1】
1 18
【样例1说明】
输入的分子为26664，分母为479952，分母可以被分子整除，输出化简后的分子为1，分母为18。
【输入样例2】
9 24
【输出样例2】
3 8
【样例2说明】
输入的分子为9，分母为24，化简后分子和分母分别为3和8，不含公约数。
【评分标准】
该题要求输出化简后的分子和分母，提交程序文件名为fraction.c。
"""


# 定义一个函数求最大公约数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    # 从控制台读入分子和分母
    numerator, denominator = map(int, input().split())

    # 计算最大公约数
    greatest_common_divisor = gcd(numerator, denominator)

    # 输出化简后的分子和分母
    print(numerator // greatest_common_divisor, denominator // greatest_common_divisor)


# 调用主函数
if __name__ == "__main__":
    main()

