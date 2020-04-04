X, H, M = (int(input()) for i in range(3))
print(((X + (H * 60) + M) // 60), ((X + (H * 60) + M) % 60), sep="\n")
