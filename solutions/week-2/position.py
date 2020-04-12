lst = [int(i) for i in input().split()]
x = int(input())

if x in lst:
    for lst_index in range(len(lst)):
        if lst[lst_index] == x:
            print(lst_index, end=" ")
else:
    print("Отсутствует")
