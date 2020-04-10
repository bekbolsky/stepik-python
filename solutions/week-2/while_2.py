a = int(input())
b = int(input())

i = 1
d = a * i

while d % a != 0 or d % b != 0:
    d = a * i
    i += 1
print(d)
