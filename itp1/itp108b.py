while True:
    x = list(map(int, input()))
    if len(x) == 1 and x[0] == 0:
        break
    print(sum(x))
