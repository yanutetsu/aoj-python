while True:
    m, f, r = list(map(int, input().split()))
    if m == -1 and f == -1 and r == -1:
        break
    t = m + f
    if m == -1 or f == -1 or t < 30:
        print("F")
    elif 80 <= t:
        print("A")
    elif 65 <= t and t < 80:
        print("B")
    elif 50 <= t and t < 65:
        print("C")
    elif 30 <= t and t < 50:
        if 50 <= r:
            print("C")
        else:
            print("D")
