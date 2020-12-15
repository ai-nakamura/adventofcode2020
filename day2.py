# * * * * * * * * * * * *
# setup
# * * * * * * * * * * * *

f = open("day2test.txt", "r")
test = f.read().split('\n')

# * * * * * * * * * * * *
# part 1
# * * * * * * * * * * * *

total_1 = 0

for lines in test:
    s = lines.split()

    lo, hi = s[0].split('-')

    lo = int(lo)
    hi = int(hi)

    key = s[1][0]

    n = s[2].count(key)

    if lo <= n <= hi:
        total_1 += 1

# print(total_1)

# * * * * * * * * * * * *
# part 2
# * * * * * * * * * * * *

total_2 = 0

for lines in test:

    s = lines.split()

    pos1, pos2 = s[0].split('-')

    pos1 = int(pos1)
    pos2 = int(pos2)

    key = s[1][0]

    username = s[2]

    if (username[pos1 - 1] == key) is not (username[pos2 - 1] == key):
        total_2 += 1

print(total_2)
