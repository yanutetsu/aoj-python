def getSortedInput():
    s = list(map(int, input().split()))
    s.sort()
    return s


s = getSortedInput()
while s[0] != 0 or s[1] != 0:
    print(" ".join(map(str, s)))
    s = getSortedInput()
