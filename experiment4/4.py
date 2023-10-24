"""
象限判定 - 实验6 条件与分支 -《Python编程基础及应用实验教程》(高等教育出版社)
【问题描述】
请编程实现下述功能：
使用代码x,y = eval(input())从键盘读入不为零的两个坐标值（浮点数）；注意两个坐标值应使用英文逗号分隔；
结合下图，判定点(x,y)所在的象限。
说明：程序约定x和y值不为0。
【输入形式】
x,y
【输出形式】
第1象限 或 第2象限 或 第3象限 或 第4象限
【样例输入】
15.2,-11.3
【样例输出】
第4象限
"""

# 从键盘读取x, y坐标值
x, y = eval(input())

# 判断坐标所在的象限
if x > 0 and y > 0:
    print("第1象限")
elif x < 0 and y > 0:
    print("第2象限")
elif x < 0 and y < 0:
    print("第3象限")
else:
    print("第4象限")