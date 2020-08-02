while True:
    H, W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break

    for i in range(H):
        o = (i == 0) or (i % 2 == 0)
        for j in range(W):
            c = "#"
            if j == 0 or j % 2 == 0:
                if o:
                    c = "#"
                else:
                    c = "."
            else:
                if o:
                    c = "."
                else:
                    c = "#"
            print(c, end="")
        print()
    print()
