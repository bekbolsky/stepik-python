vhod = [int(i) for i in input().split()]
index_list = 1
vhodSort = sorted(vhod)
vyvod = []

for number in vhodSort:
    if vhodSort.count(number) > 1:
        vyvod.append(number)

for element in vyvod[:-1]:
    while vyvod.count(element) != 1:
        vyvod.pop(vyvod.index(element))
        index_list += 1

for j in vyvod:
    print(j, end=" ")
