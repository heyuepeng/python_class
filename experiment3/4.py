"""
题库：使用列表生成式生成指定范围内的偶数列
【问题描述】
输入两个数，n,m。n是偶数，产生n和m之间的偶数。不包含m。输出偶数列表。
【输入形式】
n,m
【输出形式】
直接打印列表
【样例输入】
4,11
【样例输出】
[4, 6, 8, 10]
"""

def generate_even_list():
    # 输入字符串，例如："4,11"
    input_str = input()
    # 分割字符串并转换为整数
    n, m = map(int, input_str.split(','))

    # 使用列表生成式创建一个新列表，该列表包含范围内的所有偶数
    # range(start, stop, step) 从n开始（包括n），在m结束（不包括m），步长为2（因为我们寻找的是偶数）
    even_numbers = [x for x in range(n, m, 2)]  # n已经是偶数，所以步长为2意味着所有其他数字也是偶数

    # 打印结果列表
    print(even_numbers)

# 调用函数
generate_even_list()
