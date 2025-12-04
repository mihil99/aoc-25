
import math

filename = "1.input"

# part 1
t = 50
c = 0
with open(filename) as file:
    for line in file:
        s = 1
        if line[0] == 'L':
            s = -1
        t = (t + s*int(line[1:]))%100
        if t == 0:
            c += 1

print(f"answer 1: {c}")


# part 2
t = 50
c = 0

with open(filename) as file:
    i = 0
    for line in file:
        # print(f"t: {t} c: {c} input: {line}")
        s = 1 if line[0]=='R' else -1
        x = int(line[1:])
        t_new =  t + s*x
        if s == 1:
            c += math.floor(t_new / 100) - math.floor(t/100)
        else:
            c += math.ceil(t / 100) - math.ceil(t_new/100)
        t = t_new

print(f"answer 2: {c}")
