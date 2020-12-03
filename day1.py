# setup
f = open("day1test.txt", "r")
test = f.read().split()


# assumption: list is never < 2
def is2020_2():
    while test.__len__() > 2:
        index = int(test.pop())  # type: int
        for n in test:
            if int(n) + index == 2020:
                print(int(n), index)
                return int(n) * index


def is2020_3():
    while test.__len__() > 2:
        index = int(test.pop())
        sums = look_for_sum(2020 - index)
        if index + sums[0] + sums[1] == 2020:
            print(index, sums[0], sums[1])
            return index * sums[0] * sums[1]


def look_for_sum(total):
    """

    :type total: int
    """
    t = test[:]
    while t.__len__() > 2:
        index = int(t.pop())
        for n in t:
            if int(n) + index == total:
                return int(n), index
    return 0, 0


print(is2020_2())
# print(is2020_3())


"""
arr =\
    [ 1470,
    1644,
    1054,
    1962,
    376,
    1123,
    1683,
    1176,
    1917]


# forloop line 41
seen = [booleans] => all false

# forloop line 45
i = 376
j = TARGET - i => 1644
 

if (see[j] != true): seen[i] = true; seen[1470], seen[1644], seen[1054], seen[1962]

else: print( i * j )



"""









