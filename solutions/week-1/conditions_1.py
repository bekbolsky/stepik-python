A, B, H = (int(input()) for i in range(3))

if A <= B:
    if H > B:
        print("Пересып")
    elif H >= A and H <= B:
        print("Это нормально")
    else:
        print("Недосып")
else:
    print("Получаемое число A больше чем B!")
