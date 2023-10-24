"""
矩阵运算
【问题描述】
读入一个正整数n（1≤n≤20），再读入n行n列共n²个整数并存入由二维数组表示的方阵m；计算并输出每一行的元素和；计算并输出每一列的元素和；计算并输出对角线上的元素和（即所有m[i][i]的和, i取0~n-1）。（题目来自拼题海洋饼干叔叔）
【输入形式】
一个正整数n（1≤n≤20），再读入n行n列
【输出形式】
见样例
【样例输入】
3
1 2 3
4 5 6
7 8 10
【样例输出】
sum of row 1 = 6.
sum of row 2 = 15.
sum of row 3 = 25.
sum of column 1 = 12.
sum of column 2 = 15.
sum of column 3 = 19.
sum of elements on the diagonal = 16.
"""


def main():
    # 读入n
    n = int(input())

    # 读入矩阵
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 计算每一行的和
    for i in range(n):
        print("sum of row {} = {}.".format(i + 1, sum(matrix[i])))

    # 计算每一列的和
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        print("sum of column {} = {}.".format(j + 1, col_sum))

    # 计算对角线上的元素和
    diag_sum = 0
    for i in range(n):
        diag_sum += matrix[i][i]
    print("sum of elements on the diagonal = {}.".format(diag_sum))


# 调用主函数
if __name__ == "__main__":
    main()

