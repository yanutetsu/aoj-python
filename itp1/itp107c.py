r, c = list(map(int, input().split()))
ans = [[0 for j in range(c + 1)] for i in range(r + 1)]
for i in range(r):
    s = list(map(int, input().split()))
    for j in range(len(s)):
        ans[i][j] = s[j]
        ans[i][-1] += s[j]
        ans[-1][j] += s[j]
    ans[-1][-1] += ans[i][-1]

for i in range(len(ans)):
    print(*ans[i])
