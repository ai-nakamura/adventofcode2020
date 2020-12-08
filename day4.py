# * * * * * * * * * * * *
# Setup
# * * * * * * * * * * * *
import re

f = open("day4test.txt", "r")
test = f.read().split('\n\n')


# print(test[0])

# transform the string into dictionary
def objectify(passbook):
    obj = []
    for p in passbook.split():
        obj.append(p.split(':'))
    return dict(obj)


# validate fields
def check_valid(obj):
    # check that all the fields exist
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in fields:
        if field not in obj:
            return False

    # check each field

    # byr (Birth Year) - four digits; at least 1920 and at most 2002
    if not 1920 <= int(obj.get('byr')) <= 2002:
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not 2010 <= int(obj.get('iyr')) <= 2020:
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not 2020 <= int(obj.get('eyr')) <= 2030:
        return False

    # hgt (Height) - a number followed by either cm or in:
    metric = obj.get('hgt')[-2:]
    if not metric == 'cm' and not metric == 'in':
        return False
    # If cm, the number must be at least 150 and at most 193.
    if metric == 'cm':
        if not 150 <= int(obj.get('hgt')[:-2]) <= 193:
            return False
    # If in, the number must be at least 59 and at most 76.
    elif metric == 'in':
        if not 59 <= int(obj.get('hgt')[:-2]) <= 76:
            return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl_pattern = re.compile('[a-f0-9]{6}')
    if not obj.get('hcl')[0] == '#' or not hcl_pattern.match(obj.get('hcl')[1:]):
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if obj.get('ecl') not in colors:
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid_pattern = re.compile('^\d{9}$')
    if not pid_pattern.match(obj.get('pid')):
        return False

    # obj_printer(obj)
    return True


def obj_printer(obj):
    """
    print out obj into table format
    for testing purposes
    """
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    s = ""
    for field in fields:
        s += "{:<10}  | ".format(obj[field])
    print(s)


def main():
    valid_passbooks = 0
    for passes in test:
        p = objectify(passes)
        if check_valid(p):
            valid_passbooks += 1
    return valid_passbooks


print(main())


'''understanding the difference between objects and dictionaries

class Something:
    def __init__(self):
        self.hi = 'hi'
    def new_name(self, str):
        self.hi = str

s = Something()
print(hasattr(s, 'hi'))         # true
print(hasattr(s, 'new_name'))   # true

d = {'k':'v', 'a':'b', 'apple':'banana'}
print(hasattr(d, 'k'))          # false
print('k' in d)                 # true

'''
