"""
题库：删除列表中的重复值 -《Python编程基础及应用》习题4-8
【问题描述】
输入一个列表，删除其中的重复值，再输出。
要求：假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个。 不同元素在列表中的相对位置不应被改变。
【输入形式】
[元素1， 元素2, ... , 元素n]
【输出形式】
[元素1，元素2, ... , 元素k]
【样例输入】
[4,3,2,3,2,4,True]
【样例输出】
[3, 2, 4, True]
【样例说明】
提示：将形如"[1,3,5]"的字符串转换成列表可以使用eval()函数。 注意，输出格式应与输出样例一致，涉及空格，逗号等。
切不可一边遍历列表，一边删除列表中的元素。
"""

def remove_duplicates():
    # 读取输入的字符串并转换为列表
    input_list = input()
    original_list = eval(input_list)

    # 创建一个新列表来存储已检查过的元素
    result_list = []

    # 从后向前遍历原始列表
    for item in reversed(original_list):
        # 如果元素不在新列表中，将其添加到新列表的开头
        if item not in result_list:
            result_list.insert(0, item)

    # 打印结果列表
    print(result_list)

# 调用函数
remove_duplicates()
