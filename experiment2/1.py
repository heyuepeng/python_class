n, m, l = map(int, input().split(','))
sequence = [n + i * l for i in range(m)]
print(sequence)
