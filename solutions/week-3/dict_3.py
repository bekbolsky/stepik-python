# определяем фиктивную функцию f(x), чтобы протестировать вывод
def f(x):
    return x + 5


n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x in d:
        print(d.get(x))
    else:
        d[x] = f(x)
        print(d.get(x))
