n = int(input())

if 0 <= n <= 1000:
    if n == 0:
        print(n, "программистов", sep=" ")
    elif n % 100 >= 10 and n % 100 <= 20:
        print(n, "программистов", sep=" ")
    elif n % 10 == 1:
        print(n, "программист", sep=" ")
    elif n % 10 >= 2 and n % 10 <= 4:
        print(n, "программиста", sep=" ")
    else:
        print(n, "программистов", sep=" ")
else:
    print("Входные данные должны быть в интервале 0≤n≤1000")
