from collections import Counter
mul = 1
for _ in range(3):
    mul *= int(input())

c = Counter(str(mul))
for i in range(10):
    if c[str(i)]:
        print(c[str(i)])
    else:
        print(0)