a = int(input())
b = int(input())
c = int(input())

max_digit = 0
min_digit = 0
digits_sum = a + b + c

if a >= b and a >= c:
    max_digit = a
    print(max_digit)
elif b >= a and b >= c:
    max_digit = b
    print(max_digit)
elif c >= a and c >= b:
    max_digit = c
    print(max_digit)
else:
    print("Отсутствует максимальное число")

if a <= b and a <= c:
    min_digit = a
    print(min_digit)
elif b <= a and b <= c:
    min_digit = b
    print(min_digit)
elif c <= a and c <= b:
    min_digit = c
    print(min_digit)
else:
    print("Отсутствует минимальное число")
print(digits_sum - (max_digit + min_digit))
