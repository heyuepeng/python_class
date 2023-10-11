x = eval(input())
y = 1
for i in range(3):
    y = (y + 1) / ((100 - x) / 100)
print(f"猴子第1天摘得{int(y)}个桃.")
