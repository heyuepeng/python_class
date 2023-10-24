"""
题库：找出不是两个列表中的共有元素，在结果列表升序没有重复元素
【问题描述】
给定两个整型列表，找出不是两者共有的元素。这些元素不重复的放入新的列表，并升序排列。输出结果列表
【输入形式】
第一行输入一个列表，包括方括号，逗号分隔
第二行输入一个列表，包括方括号，逗号分隔
【输出形式】
直接用print打印结果列表
【样例输入】
[1,2,3,4,5,6,7,8,8,9,9]
[1,2,3,4,7,7,7,10,10]
【样例输出】
[5, 6, 8, 9, 10]
"""

def find_unique_elements():
    # 读取两行输入，每行一个列表
    list_str1 = input()  # 第一个列表的字符串形式，例如："[1,2,3,4,5,6,7,8,8,9,9]"
    list_str2 = input()  # 第二个列表的字符串形式，例如："[1,2,3,4,7,7,7,10,10]"

    # 将输入的字符串转换为列表
    list1 = eval(list_str1)
    list2 = eval(list_str2)

    # 将列表转换为集合，集合数据结构自动去重且可以进行集合操作
    set1 = set(list1)
    set2 = set(list2)

    # 找出只在其中一个集合中出现的元素
    # 使用对称差集（symmetric_difference）方法，或者使用 "^" 运算符，找出不共有的元素
    unique_elements = set1 ^ set2  # 或者 set1.symmetric_difference(set2)

    # 将结果转换为列表，并进行排序
    result_list = sorted(list(unique_elements))

    # 输出结果列表
    print(result_list)

# 调用函数
find_unique_elements()
