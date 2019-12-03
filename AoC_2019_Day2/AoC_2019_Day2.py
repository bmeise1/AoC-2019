#AoC Day 2

initprogram = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0]
program = initprogram

i = 0
noun = 0
verb = 0
success = False

while noun <= 99 and not success:
    program[1] = noun
    while verb <= 99 and not success:
        program[2] = verb
        while True:
            if program[i] == 1:
                program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            elif program[i] == 2:
                program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
            elif program[i] == 99:
                output = program[0]
                break
            else:
                print("PROGRAM ERROR")
                break
            i += 4
        if output == 19690720:
            success = True
            print("ANSWER FOUND")
            print(noun, verb)
            break
        if success:
            break
        verb += 1
        program = initprogram
    if success:
        break
    noun += 1
    program = initprogram
print("SCAN COMPLETE")