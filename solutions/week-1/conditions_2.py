n = int(input())
if n >= 1900 and n <= 3000:
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Неправильный год")
