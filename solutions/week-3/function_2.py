lst = [1, 3, 3, 5]


def modify_list(original_list):
    for element in original_list[::-1]:
        if element % 2 == 1:
            del original_list[original_list.index(element)]
    for target in original_list:
        original_list[original_list.index(target)] = target // 2


modify_list(lst)

print(lst)
