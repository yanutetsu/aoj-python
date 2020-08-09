n = int(input())
a = list(map(int, input().split()))

c = 0
i = 0
while i < n:
    for j in range(n - 1, i, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            c += 1
    i += 1

print(" ".join([str(x) for x in a]))
print(c)
