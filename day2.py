# setup
f = open("day2test.txt", "r")
test = f.read().split('\n')

# print(test[0])


##### part 1 ###################

total_1 = 0

for l in test:
    s = l.split()

    min, max = s[0].split('-')

    min = int(min)
    max = int(max)

    c = s[1][0]

    n = s[2].count(c)

    if n >= min and n <= max: total_1 += 1

# print(total_1)

##### part 2 ###################

total_2 = 0

for l in test:

    s = l.split()

    pos1, pos2 = s[0].split('-')

    pos1 = int(pos1)
    pos2 = int(pos2)

    c = s[1][0]

    username = s[2]

    if (username[pos1-1] == c) is not (username[pos2-1] == c):
        total_2 += 1

print(total_2)
