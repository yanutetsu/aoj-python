s = list(map(int, input().split()))
W = s[0]
H = s[1]
x = s[2]
y = s[3]
r = s[4]

if (r <= x and x <= (W - r)) and (r <= y and y <= (H - r)):
    print("Yes")
else:
    print("No")
