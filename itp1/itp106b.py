cards = [[False for y in range(13)] for x in range(4)]
suit2num = {"S": 0, "H": 1, "C": 2, "D": 3}
num2suit = {"0": "S", "1": "H", "2": "C", "3": "D"}

n = int(input())
for i in range(n):
    s, n = input().split()
    cards[suit2num[s]][int(n) - 1] = True

for i in range(4):
    suit = num2suit[str(i)]
    for j in range(13):
        if cards[i][j] == False:
            print(suit + " " + str(j + 1))
