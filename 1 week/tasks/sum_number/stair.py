import sys

number = int(sys.argv[1])

step = 1
while number > 0:
    print(' '*(number-1)+ '#'*step)
    number -= 1
    step += 1
