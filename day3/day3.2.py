import math
with open('day3\\day3testinput.txt', 'r') as file:
    input = file.readlines()
line1_directions = input[0].split(',')
line2_directions = input[1].split(',')

def determine_points(directions_array):
    points_array = []
    x = []
    y = []
    last_x = 0
    last_y = 0
    for i in directions_array:
        direction = i[0]
        value = i[1:]
        if direction == 'R':
            x.append(last_x + int(value))
            y.append(last_y)
        elif direction == 'L':
            x.append(last_x  - int(value))
            y.append(last_y)
        elif direction == 'U':
            y.append(last_y + int(value))
            x.append(last_x )
        else:
            y.append(last_y - int(value))
            x.append(last_x )
        last_x = x[-1]
        last_y = y[-1]
    points_array.append([x,y])
    return points_array

line1 = (determine_points(line1_directions))[0]
line2 = (determine_points(line2_directions))[0]

def steps_array(line):
    steps = []
    for i in line:
        steps.append(int(i[1:]))
    return(steps)

line1_steps_array = steps_array(line1_directions)
line2_steps_array = steps_array(line2_directions)

closest_intercept = 100000
import math
with open('day3\\day3testinput.txt', 'r') as file:
    input = file.readlines()
line1_directions = input[0].split(',')
line2_directions = input[1].split(',')

def determine_points(directions_array):
    points_array = []
    x = []
    y = []
    last_x = 0
    last_y = 0
    for i in directions_array:
        direction = i[0]
        value = i[1:]
        if direction == 'R':
            x.append(last_x + int(value))
            y.append(last_y)
        elif direction == 'L':
            x.append(last_x  - int(value))
            y.append(last_y)
        elif direction == 'U':
            y.append(last_y + int(value))
            x.append(last_x )
        else:
            y.append(last_y - int(value))
            x.append(last_x )
        last_x = x[-1]
        last_y = y[-1]
    points_array.append([x,y])
    return points_array

line1 = (determine_points(line1_directions))[0]
line2 = (determine_points(line2_directions))[0]

lowest_steps = 1000000

line1_steps = 0
for coords1 in range(len(line1[0])-1):
    line2_steps = 0
    for coords2 in range(len(line2[0])-1):
        #check if this set of line 2 is straight horizontally or vertically
        if line2[0][coords2] == line2[0][coords2 + 1]:
            #line 2 vertical line
            if line1[1][coords1] == line1[1][coords1 + 1]:
                #line 1 horizontal
                if (line2[0][coords2] in range(line1[0][coords1], line1[0][coords1 + 1])) or (line2[0][coords2] in range(line1[0][coords1 + 1], line1[0][coords1])):
                    if (line1[1][coords1] in range(line2[1][coords2], line2[1][coords2 + 1])) or (line1[1][coords1] in range(line2[1][coords2 + 1], line2[1][coords2])):
                        x = abs(line2[0][coords2])
                        y = abs(line1[1][coords1])
                        xdist = abs(x - line1[0][coords1])
                        ydist = abs(y - line2[1][coords2])
                        steps1 = line1_steps + xdist
                        steps2 = line2_steps + ydist
                        print('intercept, steps1 {}, steps2 {}'.format(steps1,steps2))
                        print('total steps {}'.format(steps1+steps2))
        if line2[1][coords2] == line2[1][coords2 + 1]:
            #line 2 horizontal 
            if line1[0][coords1] == line1[0][coords1 + 1]:
                #line 1 vertical
                if (line2[1][coords2] in range(line1[1][coords1], line1[1][coords1 + 1])) or (line2[1][coords2] in range(line1[1][coords1 + 1], line1[1][coords1])):
                    if (line1[0][coords1] in range(line2[0][coords2], line2[0][coords2 + 1])) or (line1[0][coords1] in range(line2[0][coords2 + 1], line2[0][coords2])):
                        x = abs(line1[0][coords1])
                        y = abs(line2[1][coords2])
                        xdist = abs(x - line2[0][coords2])
                        ydist = abs(y - line1[1][coords1])
                        steps1 = line1_steps + xdist
                        steps2 = line2_steps + ydist
                        print('intercept, steps1 {}, steps2 {}'.format(steps1,steps2))
                        print('total steps {}'.format(steps1+steps2))
        line2_steps += line2_steps_array[coords2]
    line1_steps += line1_steps_array[coords1]

print(closest_intercept)
