# 输入整数列表
integer_list = eval(input())

# 移动0元素到列表尾部
non_zero_list = [x for x in integer_list if x != 0]
zero_count = len(integer_list) - len(non_zero_list)
adjusted_list = non_zero_list + [0] * zero_count

# 输出结果
print(adjusted_list)
