# * * * * * * * * * * * *
# Setup
# * * * * * * * * * * * *

f = open("day5test.txt", "r")
test = f.read().split()


def binary_splitter(fb, lo, hi):
    turn = 0
    if fb[0] == 'B' or fb[0] == 'R':
        turn = 1

    if len(fb) == 1:
        # print("string len 1")
        if turn == 0:
            # return lower half
            return lo
        else:
            # return upper half
            return hi

    # work
    mid = (hi - lo) // 2
    # print("")
    # print("lo: {}, hi: {}, mid: {}".format(lo, hi, mid))
    if turn == 0:
        # return lower half
        # print("value {} given, taking lower half. lo = {}, new hi = {}".format(fb[0], lo, hi - mid - 1))
        return binary_splitter(fb[1:], lo, hi - mid - 1)
    else:
        # return upper half
        # print("value {} given, taking upper half. new lo = {}, hi = {}".format(fb[0], lo + mid + 1, hi))
        return binary_splitter(fb[1:], lo + mid + 1, hi)


def find_seat(sorted_seat_ids):
    prev = sorted_seat_ids[0]
    for s in sorted(sorted_seat_ids):
        if s - prev > 1:
            return s - 1
        else:
            prev = s


def find_seat_ids():
    seat_ids = []
    for boarding_pass in test:
        row = binary_splitter(boarding_pass[:-3], 0, 127)
        column = binary_splitter(boarding_pass[-3:], 0, 7)
        seat_ids.append(row * 8 + column)
    return seat_ids


# part 1
seat_IDs = find_seat_ids()
# print(max(seat_IDs))

# part 2
# print(sorted(seat_IDs))
print(find_seat(sorted(seat_IDs)))

"""
boarding_pass = "BBFFBBFRLL"
print(boarding_pass)
# get row
row = binary_splitter(boarding_pass[:-3], 0, 127)
print(row)
# get column
column = binary_splitter(boarding_pass[-3:], 0, 7)
print(column)
print(row * 8 + column)
"""