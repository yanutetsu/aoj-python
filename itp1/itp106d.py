n, m = list(map(int, input().split()))

a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    s = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = s[j]

b = [0 for i in range(m)]
for i in range(m):
    b[i] = int(input())

c = [0 for i in range(n)]
for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]

for i in range(len(c)):
    print(c[i])
