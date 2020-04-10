s = str(input())

i = 0
counter = 1
length = len(s)

for char in s[:-1]:
    if s[i] == s[(i + 1) - length]:
        counter += 1
    else:
        print(s[i] + str(counter), end="")
        counter = 1
    i += 1

print(s[i] + str(counter), end="")
