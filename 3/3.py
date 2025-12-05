
FILENAME = "3.input"

c = 0
with open(FILENAME, 'r') as file:
    for line in file:
        nums = list(map(int, list(line.strip())))
        first = 0
        second = 0
        for i,(a,b) in enumerate(zip(nums[:-1], nums[1:])):
            # print(f"i: {i} a: {a} b: {b}")
            if a > first:
                first = a
                second = b
            if b > second:
                second = b
        c += first*10 + second


print(f"answer 1: {c}")


def max_joltage(_list: [int], length = 12):
    if length == 1:
        return [max(_list)]
    v = 0
    index = -1
    for i, num in enumerate(_list[:-length+1]):
        if num > v:
            v = num
            index = i
    return [v, *max_joltage(_list[index+1:], length-1)]


c = 0
with open(FILENAME, 'r') as file:
    for line in file:
        nums = list(map(int, list(line.strip())))
        res = max_joltage(nums)
        c += int(''.join(map(str,res)))

print(f"answer 2: {c}")
