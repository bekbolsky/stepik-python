with open("solutions/week-3/dataset_3363_2.txt") as f:
    a = f.readline().strip()
print(a)

b = []
for i in range(len(a)):
    if a[i].lower() in "qwertyuiopasdfghjklzxcvbnm":
        b += a[i]
        a = a[:i] + "!" + a[(i + 1):]
        # print(a)
c = a.split("!")[1:]
# print(c)
for i in range(len(b)):
    print(b[i] * int(c[i]), end="")
