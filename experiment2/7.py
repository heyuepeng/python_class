# 输入整数列表
integer_list = list(map(int, input().split(',')))

# 输入n和m
n, m = map(int, input().split(','))

# 检查n是否在列表下标范围内
if abs(n) >= len(integer_list):
    print("error")
else:
    # 选择第n个元素
    selected_element = integer_list[n]

    # 重复该元素m次
    repeated_elements = [selected_element] * m

    # 将重复的元素添加到列表末尾
    integer_list.extend(repeated_elements)

    # 输出结果列表
    print(integer_list)
