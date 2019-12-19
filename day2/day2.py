with open('day2\\day2input.txt', 'r') as file:
    input = file.readlines()

intcode = input[0].split(',')

for i in range(len(intcode)):
    intcode[i] = int(intcode[i])

done = False 
instruction_pointer = 0 
 
while not done:
    if intcode[instruction_pointer] == 1:
        intcode[intcode[instruction_pointer+3]] = intcode[intcode[instruction_pointer+1]] + intcode[intcode[instruction_pointer+2]]
    elif intcode[instruction_pointer] == 2:
        intcode[intcode[instruction_pointer+3]] = intcode[intcode[instruction_pointer+1]] * intcode[intcode[instruction_pointer+2]]
    elif intcode[instruction_pointer] == 99:
        done = True
        print('opcode 99: program done')
    else:
        done = True
        print('unknown opcode: somethings wrong')
    instruction_pointer += 4

print(intcode[0])