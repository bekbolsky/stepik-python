n = int(input())

number_sequence = []

for i in range(1, n + 1):
    while number_sequence.count(i) != i and len(number_sequence) != n:
        number_sequence.append(i)

for element in number_sequence:
    print(element, end=" ")
