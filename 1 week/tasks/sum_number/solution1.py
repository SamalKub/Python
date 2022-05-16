import sys

digit_string = sys.argv[1]

sum_el = sum([int(el) for el in digit_string])

print(sum_el)
