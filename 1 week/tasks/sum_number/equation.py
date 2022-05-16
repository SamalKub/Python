import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = (b**2 - 4 *a * c)**0.5
x1, x2 = (-b + D) / (2*a), (-b - D) / (2*a)
print(int(x1))
print(int(x2))
