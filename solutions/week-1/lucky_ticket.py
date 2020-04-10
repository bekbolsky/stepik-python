number = str(input())

# разделение числа на две части
first_half = int(number) // 1000
second_half = int(number) % 1000

# цифры первой половины
first = first_half // 100
second = first_half % 100 // 10
third = first_half % 100 % 10

# цифры второй половины
fourth = second_half // 100
fifth = second_half % 100 // 10
sixth = second_half % 100 % 10

if first + second + third == fourth + fifth + sixth:
    print("Счастливый")
else:
    print("Обычный")
