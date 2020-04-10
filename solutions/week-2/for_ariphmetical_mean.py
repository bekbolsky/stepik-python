a, b = (int(input()) for number in range(2))

s = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        counter += 1
        s += i
print(s / counter)
