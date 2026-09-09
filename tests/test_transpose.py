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


def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


test_transpose()


def test_transpose_square_matrix():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


test_transpose_square_matrix()


def test_transpose_empty_matrix():
    assert transpose([]) == []


test_transpose_empty_matrix()


def test_transpose_single_row():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]


test_transpose_single_row()


def test_transpose_single_column():
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]


test_transpose_single_column()

print(transpose([[4, 5, 9], [1, 2, 7]]))
