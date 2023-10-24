"""
题库：把分布在两个列表中的姓名和成绩配对后形成一个列表
【问题描述】
已知一个列表中存放的是一些学生的姓名，另外一个列表存放的是学生对应的考试成绩。两个列表长度相同。要求，把姓名和对应的成绩进行组合，形成一个列表。该列表包含一个嵌套列表，每个子列都是姓名和对应的成绩。最后输出形成的新列表。
【输入形式】
分两行输入，第一行输入姓名，按照字符串的方式输入，多个姓名之间用逗号分隔。第二行输入成绩，包含方括号，元素之间用英文逗号分隔。
【输出形式】
直接用print输出新的列表。
【样例输入】
tom,jack,jone,mike
[88,89,34,90]
【样例输出】
[['tom', 88], ['jack', 89], ['jone', 34], ['mike', 90]]
"""

def pair_names_and_scores():
    # 读取姓名，并使用split方法将其分割为一个列表
    names_input = input()
    names = names_input.split(',')

    # 读取成绩列表
    scores_input = input()
    scores = eval(scores_input)  # 将输入的字符串转换为列表

    # 使用zip函数将两个列表合并，形成一个新列表，每个元素都是一个包含名字和分数的子列表
    paired_list = [[name, score] for name, score in zip(names, scores)]

    # 打印结果列表
    print(paired_list)

# 调用函数
pair_names_and_scores()
