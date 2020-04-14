matrix = []
stop_ = "end"

while True:
    line = [l for l in input().split()]
    if stop_ in line:
        break
    else:
        matrix.append(line)

new_matrix = []

for i in range(len(matrix)):
    new_matrix.append([])
    for j in range(len(matrix[i])):
        if len(matrix) == 1:
            new_matrix[i].append(
                str(
                    int(matrix[i - 1][j])
                    + int(matrix[i + 1 - len(matrix)][j])
                    + int(matrix[i][j - 1])
                    + int(matrix[i][j + 1 - len(matrix[i])])
                )
            )
        elif len(matrix) >= 2 and len(matrix[i]) == 1:
            new_matrix[i].append(
                str(
                    int(matrix[i - 1][j])
                    + int(matrix[i + 1 - len(matrix)][j])
                    + int(matrix[i][j - 1])
                    + int(matrix[i][j + 1 - len(matrix[i])])
                )
            )
        else:
            if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
                new_matrix[i].append(
                    str(
                        int(matrix[i - 1 - len(matrix)][j - len(matrix[i])])
                        + int(matrix[i + 1 - len(matrix)][j - len(matrix[i])])
                        + int(matrix[i - len(matrix)][j - 1 - len(matrix[i])])
                        + int(matrix[i - len(matrix)][j + 1 - len(matrix[i])])
                    )
                )

            elif i == len(matrix) - 1:
                new_matrix[i].append(
                    str(
                        int(matrix[i - 1 - len(matrix)][j])
                        + int(matrix[i + 1 - len(matrix)][j])
                        + int(matrix[i][j - 1])
                        + int(matrix[i][j + 1])
                    )
                )
            elif j == len(matrix[i]) - 1:
                new_matrix[i].append(
                    str(
                        int(matrix[i - 1][j])
                        + int(matrix[i + 1][j])
                        + int(matrix[i][j - 1 - len(matrix[i])])
                        + int(matrix[i][j + 1 - len(matrix[i])])
                    )
                )
            else:
                new_matrix[i].append(
                    str(
                        int(matrix[i - 1][j])
                        + int(matrix[i + 1][j])
                        + int(matrix[i][j - 1])
                        + int(matrix[i][j + 1])
                    )
                )

# print(new_matrix)
for n in range(len(new_matrix)):
    for st in new_matrix[n]:
        print(st, end=" ")
    print()
