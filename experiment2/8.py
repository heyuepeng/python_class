# 输入由空格分隔的多个字符串构成的列表
string_list = input().split()

# 输入两个整数n和m
n, m = map(int, input().split())

# 检查n和m是否在列表下标范围内
if 0 <= abs(n) < len(string_list) and 0 <= abs(m) < len(string_list):
    # 交换位置n和m的两个元素的值
    string_list[n], string_list[m] = string_list[m], string_list[n]

    # 输出交换后的列表
    print(string_list)
else:
    print("error")