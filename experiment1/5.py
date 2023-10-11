import math

r1 = float(input()) / 2
r2 = float(input()) / 2
v = 4 / 3 * math.pi * (math.pow(r1, 3) + math.pow(r2, 3))

l = round(math.pow(v, 1 / 3), 2)

# 输出结果，保留两位小数
print("正方体边长为:{:.2f}.".format(l))
