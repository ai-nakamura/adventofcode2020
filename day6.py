# * * * * * * * * * * * *
# Setup
# * * * * * * * * * * * *
f = open("day6test.txt", "r")
test = f.read().split('\n\n')

"""
* * * * * * * *
*    Part 1   *
* * * * * * * *

def process_one_yes(group):
    yeses = [0 for _ in range(26)]
    for respondent in group.split():
        answers = respondent.split()
        for a in answers[0]:
            yeses[ord(a) - 97] = 1
    return yeses


def main():
    total = 0
    for groups in test:
        one_group = process_one_yes(groups)
        total += sum(one_group)
    return total
"""


"""
* * * * * * * *
*    Part 2   *
* * * * * * * *
"""


def everyone_yes(str_group):
    """
    takes in one group (not a list of them) and finds the responses that everyone answered yes to
    :param str_group: string representation of one group
    :return: number of answers everyone said yes to
    """
    respondent = str_group.split()
    # print(respondent)

    if len(respondent) < 1:
        print("that didn't have anything")
        return 0

    yeses = [0 for _ in range(26)]

    # do the first person
    for a in respondent[0]:
        yeses[ord(a) - 97] = 1

    # do the rest
    if not len(respondent) == 1:
        for resp in respondent[1:]:
            this_one = [0 for _ in range(26)]
            for a in resp:
                this_one[ord(a) - 97] = 1
            yeses = [a and b for a, b in zip(yeses, this_one)]
            print(yeses)

    return yeses


def main():
    total = 0
    for groups in test:
        one_group = everyone_yes(groups)
        total += sum(one_group)
    return total


"""
* * * * * * * *
*   Testing   *
* * * * * * * *
"""

g = "a\
    bz\
    cd"
g2 = "ab\
     ac"

# break down of test[-1]
a = [ch for ch in 'nlczsygmdabuorweqjhxfitv']
a.sort()
b = [ch for ch in 'nmuvojghteyaxibwldsqrzfc']
b.sort()
c = [ch for ch in 'mihetjnswbyzdvufcogxaqrl']
c.sort()
d = [c for c in 'iulxgqfoctnjhvrawbzemsdy']
d.sort()
e = [c for c in 'exugdvclmqfzsojiwnbarhty']
e.sort()

# part 1
# print(sum(process_one_yes(g)))
# print(main())

# part 2
# print(everyone_yes("abc"))
print(everyone_yes(g2))
print(main())
