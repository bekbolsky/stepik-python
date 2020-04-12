s = [int(input())]

while sum(s) != 0:
    s.append(int(input()))

print(sum(j**2 for j in s))
