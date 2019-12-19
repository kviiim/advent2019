import math 
file = open('day1\\day1input.txt','r')

total = 0
for line in file.readlines():
    subtotal = 0
    all_vals = []
    subtotal += math.floor(int(line)/3) - 2
    all_vals.append(subtotal)
    while all_vals[-1] > 0:
        next_mass = math.floor(all_vals[-1]/3) - 2
        if next_mass < 0:
            next_mass = 0
        all_vals.append(next_mass)
        subtotal += next_mass
    total += subtotal

print(total)