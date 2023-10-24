"""
百人搬百砖/百钱买百鸡 - 实验9 循环进阶 - 《Python编程基础及应用实验教程》(高等教育出版社)
【问题描述】
百人搬百砖问题是中国古代百钱买百鸡问题的另一种表达形式。
工地搬砖，男人一人搬3块，女人一人搬2块，小孩两人搬1块。n个人搬n块砖，总共有哪些搬法？

请参考伪代码将下述程序补充完整，并上机调试运行。
注意：程序还应确保小孩数可以整数2，即小孩数必须为偶数。
"""

N = int(input())

count = 0

for man in range(0, N+1):
    for woman in range(0, N+1):
        for child in range(0, N+1, 2):  # 步长为2，确保小孩数量为偶数
            if man + woman + child == N and man * 3 + woman * 2 + child // 2 == N:
                print(f"男人:{man}, 女人:{woman}, 小孩:{child}")
                count += 1

print(f"总共有{count}种搬法。")

