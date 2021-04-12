def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key not in d and (2 * key) in d:
        d[2 * key].append(value)
    elif key not in d and (2 * key) not in d:
        d[2 * key] = [value]


# dict = {1: [0]}
dict = {}

update_dictionary(dict, 1, -1)
update_dictionary(dict, 2, -2)
update_dictionary(dict, 1, -3)

print(dict)
