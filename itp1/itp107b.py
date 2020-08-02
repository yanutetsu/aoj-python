import math

while True:
    n, x = list(map(int, input().split()))
    if n == 0 and x == 0:
        break
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i == j:
                continue
            for k in range(j + 1, n + 1):
                if k == i or k == j:
                    continue
                if i + j + k == x:
                    count += 1
    print(count)
