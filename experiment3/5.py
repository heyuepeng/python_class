"""
题库：找出列表中的多数元素
【问题描述】
  读入一个大小为n的列表，找出其中的多数元素。多数元素是指在列表中出现次数大于n//2的元素（每个列表最多一个多数元素）。根据代码框架编写一个函数。
【输入形式】
输入列表，包括方括号，逗号分隔
【输出形式】
如果有多数元素，输出这个元素的值，如果没有多数元素，输出False
【样例输入】
[3,2,3]
【样例输出】
3
"""

def find_majority_element():
    # 读取输入列表
    input_list = input()
    nums = eval(input_list)  # 将输入的字符串转换为列表

    # 创建一个字典来存储每个元素及其出现的次数
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # 计算多数元素的阈值
    majority_count = len(nums) // 2

    # 检查是否有元素满足多数元素的条件
    for num, count in count_dict.items():
        if count > majority_count:
            print(num)  # 如果找到多数元素，则打印并退出函数
            return

    print(False)  # 如果没有找到多数元素，则打印False

# 调用函数
find_majority_element()
