
FILEPATH = '5.input'

ranges = []
ingredients = []

with open(FILEPATH, 'r') as file:
    lines = file.readlines()
    i = 0
    while lines[i].strip() != '':
        ranges.append(list(map(int, lines[i].split('-'))))
        i += 1
    i += 1
    while i < len(lines):
        ingredients.append(int(lines[i]))
        i += 1

total = 0
for ingredient in ingredients:
    for _range in ranges:
        if _range[0] <= ingredient and ingredient <= _range[1]:
            total += 1
            break

print(f"answer 1: {total}")


clean_list = []


def overlap(range1, range2):
    if (range1[0] <= range2[0] and range2[0] <= range1[1]) \
            or (range2[0] <= range1[0] and range1[0] <= range2[1]) \
            or (range1[0] <= range2[1] and range2[1] <= range1[1]) \
            or (range2[0] <= range1[1] and range1[1] <= range2[1]):
        return [min(range1[0], range2[0]), max(range1[1], range2[1])]
    return None


result_ranges = []
new_ranges = ranges.copy()
r = new_ranges[0]
new_ranges.remove(r)
while True:
    found_something = False
    for new_range in new_ranges:
        o = overlap(r, new_range)
        if o:
            found_something = True
            r = o
            new_ranges.remove(new_range)
            break
    if not found_something:
        result_ranges.append(r)
        if len(new_ranges) == 0:
            break
        r = new_ranges[0]

total = 0
for r in result_ranges:
    total += r[1] - r[0] + 1

print(f"answer 2: {total}")
