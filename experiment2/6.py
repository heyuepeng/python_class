# 输入正整数列表
integer_list = eval(input())
# 排序列表，将数字按照最高位进行排序
sorted_list = sorted(integer_list, reverse=True)
# 将数字按位组织成最大整数
max_integer = int(''.join(map(str, sorted_list)))
# 输出结果
print(max_integer)
