# * * * * * * * * * * * *
# Setup
# * * * * * * * * * * * *

f = open("day3test.txt", "r")
test = f.read().split('\n')
# print(test[0])


# * * * * * * * * * * * *
# Part 1
# Move 3 right, 1 down
#
# PArt 2 - modified to take in travel angles instead of hard coding for part 1
# * * * * * * * * * * * *

# Global
traveler = [0, 0]
mapEdge = test[0].__len__()
treeCtr = 0
tree = 'X'

print(traveler, mapEdge, treeCtr, tree)


def travel(x, y):
    global traveler, mapEdge, treeCtr, tree

    # Move 3 right
    traveler[0] += x
    # Check if we've reached the edge. If yes, start back at the left of the map
    if traveler[0] >= mapEdge:
        traveler[0] -= mapEdge

    # Move 1 down
    traveler[1] += y
    # Check if we've reached the bottom of the map
    if traveler[1] >= test.__len__()-1:
        print("Done. Slope (" + str(x) + ", " + str(y) + ") encountered " + str(treeCtr) + " trees.")

    # Check if we've hit a tree
    # print(list(test[traveler[0]])[traveler[1]])
    if list(test[traveler[1]])[traveler[0]] == '#':
        treeCtr += 1

    # print map
    mark_map = list(test[traveler[1]])
    if mark_map[traveler[0]] == '#':
        mark_map[traveler[0]] = tree
    else:
        mark_map[traveler[0]] = 'O'

    # print("".join(mark_map))

# for x in range(0, test.__len__()-1):
    # travel(1, 1) # 87
    # travel(3, 1) # 205
    # travel(5, 1) # 85
    # travel(7, 1) # 79
    # travel(1, 2) # 33
# print(traveler, mapEdge, treeCtr, tree)
