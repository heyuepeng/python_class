# 输入整数列表
integer_list = eval(input())

# 查找最大值和最小值
max_value = max(integer_list)
min_value = min(integer_list)

# 删除所有的最大值和最小值
filtered_list = [x for x in integer_list if x != max_value and x != min_value]

# 输出结果
print(filtered_list)
