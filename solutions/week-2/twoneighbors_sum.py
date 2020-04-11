list_of_num = [int(i) for i in input().split()]
length = len(list_of_num)
second_list = []

if length == 1:
    second_list.append(list_of_num[0])
else:
    for element in list_of_num[:-1]:
        second_list.append(
            list_of_num[list_of_num.index(element) - 1]
            + list_of_num[list_of_num.index(element) + 1]
        )
    second_list.append(list_of_num[length - 2] + list_of_num[0])

for j in second_list:
    print(j, end=" ")
