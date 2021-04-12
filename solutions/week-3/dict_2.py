stroka = [str(i) for i in input().lower().split()]


def count_words(any_string):
    s = set(any_string)
    for element in s:
        amount = any_string.count(element)
        print(element, amount)


count_words(stroka)
