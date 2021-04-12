with open("solutions/week-3/dataset_3363_3.txt") as f:
    content = f.read().strip().split()


def most_frequent(words_list):
    sorted_words = sorted(words_list)
    lowered = [word.lower() for word in sorted_words]
    maximal = 0

    for word in lowered:
        word_count = lowered.count(word)
        if word_count > maximal:
            maximal = word_count
            print(word, maximal)

    # решение со словарём
    # uniques = set(lowered)
    # words_count = {}
    # for elem in uniques:
    #     amount = lowered.count(elem)
    #     words_count[elem] = amount

    # maximal = max(words_count.values())

    # frequents = []
    # for k, v in words_count.items():
    #     if v == maximal:
    #         frequents.append(k)

    # for k, v in words_count.items():
    #     if k == sorted(frequents)[0]:
    #         print(k, v)


most_frequent(content)
