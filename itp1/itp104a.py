import math

a, b = list(map(int, input().split()))

d = math.floor(a / b)
r = a % b
f = a / b

print(str(d) + " " + str(r) + " " + f"{f:f}")
