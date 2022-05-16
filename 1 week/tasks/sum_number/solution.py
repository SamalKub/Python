import sys

number = int(sys.argv[1])

step = 1
while number > 0:
    print(' '*(number-1)+ '#'*step)
    number -= 1
    step += 1

# num_steps = int(sys.argv[1])

# for i in range(num_steps):
#     print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
