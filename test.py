a = [1, 2, 3]

b = []
for i in a:
    b.extend([i for _ in range(10)])

print(b)