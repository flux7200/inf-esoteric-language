from sys import argv
import math, getch

def usage():
    if len(argv) != 2:
        print("Usage: inf [FILENAME].infinity")
        exit(1)

def get_program():
    try:
        with open(argv[1]) as file:
            program = file.read()
        return program
    except:
        print(argv[1] + " is not a file.")
        exit(1)

def get_usable_chars(program):
    chars = []

    for line in program.split('\n'):
        for char in line:
            if char == "I":
                chars.append("I")

            elif char == "N":
                chars.append("N")

            elif char == "F":
                chars.append("F")

            elif char == "%":
                break

    return chars

def chars_to_instructions(chars):
    ptr = 1
    prog = []

    for char in chars:
        if char == "I":
            ptr += 1

        elif char == "N":
            ptr -= 1

        elif char == "F":
            prog.append(ptr)

    return prog

def main():
    usage()

    prog = chars_to_instructions(get_usable_chars(get_program()))

    memory = [0]
    mp = 0

    for inst in prog:
        # Dynamic Memory
        if inst == 1:
            memory[mp] += 1

        elif inst == 2:
            memory[mp] -= 1

        elif inst == 3:
            mp -= 1
            if mp == len(memory):
                memory.append(0)

        elif inst == 4:
            mp += 1
            if mp < 0:
                memory.insert(0, 0)
                mp = 0

        elif inst == 5:
            if mp + 1 == len(memory):
                memory.append(memory[mp])
            else:
                memory[mp + 1] = memory[mp]

        # Arithmetic
        elif inst == 11:
            if mp + 1 == len(memory):
                memory.append(0)
            else:
                memory[mp] += memory[mp + 1]

        elif inst == 12:
            if mp + 1 == len(memory):
                memory.append(0)
            else:
                memory[mp] -= memory[mp + 1]

        elif inst == 13:
            if mp + 1 == len(memory):
                memory.append(0)
                memory[mp] = 0
            else:
                memory[mp] *= memory[mp + 1]

        elif inst == 14:
            if mp + 1 == len(memory) or memory[mp + 1] == 0:
                print("ERROR! Division by 0 occured.")
                exit(1)
            else:
                memory[mp] /= memory[mp + 1]

        elif inst == 15:
            memory[mp] = math.sqrt(memory[mp])

        elif inst == 16:
            memory[mp] = math.sin(memory[mp])

        elif inst == 17:
            memory[mp] = math.cos(memory[mp])

        elif inst == 18:
            memory[mp] = math.asin(memory[mp])

        elif inst == 19:
            memory[mp] = math.acos(memory[mp])

        # Console Output
        elif inst == 21:
            print(memory[mp])

        elif inst == 22:
            print(chr(memory[mp]), end = '')

        # Console Input
        elif inst == 31:
            memory[mp] = float(input())

        elif inst == 32:
            memory[mp] = ord(getch.getch())

if __name__ == '__main__':
    main()
