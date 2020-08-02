n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 or i % 10 == 3 or ("3" in list(str(i))):
        print(" " + str(i), end="")
print()
