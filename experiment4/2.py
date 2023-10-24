"""
题库：打印拐形图案
【问题描述】
打印一个如样例输出所示的拐形图案。
【输入形式】
一个整数n,表示图案的总行,1<=n<20
【输出形式】
一个图案
【样例输入】
6
【样例输出】
"""


n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+j), end="")
    for j in range(i+1, n+1):
        print(chr(64+i), end="")
    print()



