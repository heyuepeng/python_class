# 输入整数列表
integer_list = eval(input())

# 计算平均值
average = sum(integer_list) / len(integer_list)

# 根据平均值是否有小数部分输出结果
if average.is_integer():
    print(int(average))
else:
    print(f'{average:.2f}')
