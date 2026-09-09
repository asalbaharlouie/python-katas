def transpose(matrix):
    if matrix == []:
        return []
    result = []
    for i in range(len(matrix[0])):  # روی ستون راه میره
        new_rows = []
        for j in range(len(matrix)):  # روی سطر راه میره
            new_rows.append(matrix[j][i])
        result.append(new_rows)

    return result


print(transpose([[4, 5, 9], [1, 2, 7]]))
