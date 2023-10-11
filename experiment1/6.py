# 从键盘读取大写字母Q
Q = input(" ")

# 计算Q所代表的大写字母在字母表中的位置
position_Q = ord(Q) - ord('A') + 1

# 输出结果
print("{}是字母表中第{}个字母.".format(Q, position_Q))

# 从键盘读取整数N
N = int(input(""))

# 计算第N个字母是什么
letter_N = chr(ord('A') + N - 1)

# 输出结果
print("字母表中第{}个字母是{}.".format(N, letter_N))
