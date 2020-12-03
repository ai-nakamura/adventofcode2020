# setup
f = open("day2test.txt", "r")
test = f.read().split('\n')

# print(test[0])


total = 0

for l in test:
    s = l.split()

    min, max = s[0].split('-')

    min = int(min)
    max = int(max)

    c = s[1][0]

    n = s[2].count(c)

    if (n >= min and n <= max): total += 1

print(total)