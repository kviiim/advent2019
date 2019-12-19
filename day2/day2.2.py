with open('day2\\day2input.txt', 'r') as file:
    input = file.readlines()

original_intcode = input[0].split(',')
for i in range(len(original_intcode)):
    original_intcode[i] = int(original_intcode[i])

goal_output = 19690720

def run_program(noun,verb):
    done = False 
    instruction_pointer = 0 
    intcode = original_intcode.copy()
    intcode[1] = noun
    intcode[2] = verb
    while not done:
        if intcode[instruction_pointer] == 1:
            intcode[intcode[instruction_pointer+3]] = intcode[intcode[instruction_pointer+1]] + intcode[intcode[instruction_pointer+2]]
        elif intcode[instruction_pointer] == 2:
            intcode[intcode[instruction_pointer+3]] = intcode[intcode[instruction_pointer+1]] * intcode[intcode[instruction_pointer+2]]
        elif intcode[instruction_pointer] == 99:
            done = True
        else:
            done = True
        instruction_pointer += 4
    if intcode[0] == goal_output:
        return True
    else:
        return False

for noun in range(99):
    for verb in range(99):
        outcome = run_program(noun,verb)
        if outcome == True:
            print(100 * noun + verb)
            break
    if outcome == True:
        break