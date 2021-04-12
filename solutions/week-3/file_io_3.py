with open("solutions/week-3/dataset_3363_4.txt") as f:
    content = f.read().strip().splitlines()


mathematics = 0
physics = 0
rus_lang = 0
length = len(content)

for line in content:
    info = line.split(";")
    sum = 0

    for mark in info[1:]:
        sum += int(mark)
    print(sum / len(info[1:]))

    mathematics += int(info[1])
    physics += int(info[2])
    rus_lang += int(info[3])

print(mathematics / length, physics / length, rus_lang / length)
