# 输入列表
lst = eval(input())

# 输入n和m
n, m = map(int, input().split(','))

# 检查n和m是否在列表范围内
if n < 0 or m > len(lst) or n >= m:
    print("error")
else:
    del lst[n:m]
    print(lst)
