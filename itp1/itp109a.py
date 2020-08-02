w = input()

t = []
while True:
    buf = input().split()
    if buf[-1] == "END_OF_TEXT":
        break
    t += [x.lower() for x in buf]

print(t.count(w))
