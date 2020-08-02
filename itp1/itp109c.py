taro = 0
hanako = 0

n = int(input())
for i in range(n):
    t, h = input().split()
    if t < h:
        hanako += 3
    elif t == h:
        taro += 1
        hanako += 1
    elif h < t:
        taro += 3
print("%d %d" % (taro, hanako))
