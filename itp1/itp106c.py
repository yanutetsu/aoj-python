buildings = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

n = int(input())
for i in range(n):
    b, f, r, v = list(map(int, input().split()))
    buildings[b - 1][f - 1][r - 1] += v

for b in range(len(buildings)):
    if 0 < b:
        print("#" * 20)

    for f in range(len(buildings[b])):
        for r in range(len(buildings[b][f])):
            print(" " + str(buildings[b][f][r]), end="")
        print()
