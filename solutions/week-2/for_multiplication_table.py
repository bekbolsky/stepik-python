a, b, c, d = (int(input()) for number in range(4))

if (a <= 10) and (b <= 10) and (c <= 10) and (d <= 10):
    if (a <= b) and (c <= d):
        for element in range(c, d + 1):
            print("\t", element, end="")
        print()
        for i in range(a, b + 1):
            print(i, end="\t")
            for j in range(c, d + 1):
                print(i * j, end="\t")
            print()
else:
    print("Числа не из заданного отрезка!")
