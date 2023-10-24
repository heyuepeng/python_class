"""
题库：把数列的元素重复n次，然后元素的平方形成新列表，然后去除重复元素
【问题描述】
读入一个整数列表和正整数n(n>1)，把列表中每个元素重复n次，并对每个元素进行平方形成新的列表，最后去除列表中的重复元素。打印输出新列表。
【输入形式】
第一行输入列表，包括方括号，元素之间用逗号分隔。
第二行输入重复的次数。
【输出形式】
直接用print输出列表
【样例输入】
[2,3,4,5,5]
5
【样例输出】
[4, 9, 16, 25]
"""


def create_and_process_list():
    # 读取输入数据
    input_list = input()  # 读取列表，例如："[2,3,4,5,5]"
    n = int(input())  # 读取重复次数，例如：5

    # 将字符串格式的列表转换为实际的列表数据结构
    original_list = eval(input_list)

    # 创建一个空集合用于检测重复的平方数
    seen_squares = set()
    # 创建一个空列表用于存储非重复的平方数，同时保持它们的原始顺序
    unique_squares = []

    for number in original_list:
        square = number ** 2  # 计算当前数字的平方
        if square not in seen_squares:  # 如果这个平方数是唯一的（之前未见过）
            seen_squares.add(square)  # 标记这个平方数为已见过，以便未来检测重复
            unique_squares.append(square)  # 将这个唯一的平方数添加到结果列表中

    # 由于我们在构建列表的过程中排除了重复项，因此无需排序，直接打印列表即可
    print(unique_squares)

# 调用函数
create_and_process_list()


