figure = str(input())
if figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(S)
elif figure == "прямоугольник":
    a = int(input())
    b = int(input())
    S = float(a * b)
    print(S)
elif figure == "круг":
    r = int(input())
    pi = float(3.14)
    S = pi * (r ** 2)
    print(S)
else:
    print("Другая фигура")
