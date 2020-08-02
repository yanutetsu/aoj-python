import math

op = ""
while True:
    s = input().split()

    a = int(s[0])
    op = s[1]
    b = int(s[2])

    ans = ""
    if op == "?":
        break
    elif op == "+":
        ans = a + b
    elif op == "-":
        ans = a - b
    elif op == "*":
        ans = a * b
    elif op == "/":
        ans = math.floor(a / b)

    print(ans)
