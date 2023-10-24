"""
题库：在列表中找出只出现一次的元素，并排序输出
【问题描述】
输入一个自然数列表，找出只出现一次的元素，并升序输出。如果没有只出现一次的元素，则输出False。
【输入形式】
输入包含自然数的列表，包括方括号，逗号分隔
【输出形式】
排序后的数字，每个数字之间用英文逗号分隔。或者False。
【样例输入1】
[1,2,3,5,2,3,4]
【样例输出1】
1,4,5
【样例输入2】
[9,9,9,12,12]
【样例输出2】
False
【样例说明】
[9,9,9,12,12]列表中，9出现3次，12出现2次，没有出现一次的元素，则输出False。
"""

def find_unique_elements():
    # 读取输入字符串并转换为列表
    input_str = input()
    num_list = eval(input_str)

    # 创建一个字典来存储每个数字及其出现的次数
    count_dict = {}
    for num in num_list:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # 找出只出现一次的元素
    unique_elements = [num for num, count in count_dict.items() if count == 1]

    # 检查是否有只出现一次的元素
    if unique_elements:
        # 如果有，则对这些元素进行排序
        unique_elements.sort()
        # 按照要求的格式打印输出结果
        print(','.join(map(str, unique_elements)))
    else:
        # 如果没有符合条件的元素，输出"False"
        print(False)

# 调用函数
find_unique_elements()

