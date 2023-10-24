"""
题库：计算列表的度
【问题描述】
对于一个包含自然数的列表nums，计算他的度。列表的度定义为列表里任一元素出现的频率的最大值。
【输入形式】
从键盘输入一个列表，包含方括号，逗号分隔
【输出形式】
整数
【样例输入】
[1,2,3,3,4,5,4,3,3]
【样例输出】
4
【样例说明】
列的所有元素的频率中，元素3的频率最大为4.
【评分标准】
通过测试数据
"""


def find_degree_of_list():
    # 输入字符串，例如："[1,2,3,3,4,5,4,3,3]"
    input_str = input()

    # 将字符串转换为列表，例如：[1,2,3,3,4,5,4,3,3]
    nums = eval(input_str)

    # 创建一个字典来存储每个数字的频率
    frequency_dict = {}
    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1  # 如果数字已存在，增加计数
        else:
            frequency_dict[num] = 1  # 否则，初始化为1

    # 找到出现次数最多的频率
    max_frequency = max(frequency_dict.values())

    # 打印结果
    print(max_frequency)


# 调用函数
find_degree_of_list()
