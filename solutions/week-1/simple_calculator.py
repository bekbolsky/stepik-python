first = float(input())
second = float(input())
op = str(input())

if second == 0 and (op == "/" or op == "mod" or op == "div"):
    print("Деление на 0!")
elif op == "+":
    print(first + second)
elif op == "-":
    print(first - second)
elif op == "*":
    print(first * second)
elif op == "/":
    print(first / second)
elif op == "mod":
    print(first % second)
elif op == "pow":
    print(first ** second)
elif op == "div":
    print(first // second)
else:
    print("Неизвестная операция над числами")
