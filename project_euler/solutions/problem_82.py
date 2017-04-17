from numpy import cumsum

from ..framework.load_file import load_file


def solve(name: str='matrix.txt', relative: bool=True):
    matrix_raw = load_file(82, name, relative)

    matrix = [[int(n) for n in line.split(',')]
              for line in matrix_raw.split('\n') if line]

    rows = len(matrix)
    columns = len(matrix[0])

    # take transpose, because it makes more sense
    matrix = [[matrix[i][j] for i in range(rows)] for j in range(columns)]

    shadow_matrix = [[0 for _ in line] for line in matrix]

    for j in range(columns - 1, -1, -1):
        cost = cumsum(matrix[j])
        for i in range(rows):
            if j == columns - 1:
                shadow_matrix[j][i] = matrix[j][i]
            else:
                possible = [cost[i] - cost[k] + matrix[j][k] +
                            shadow_matrix[j + 1][k] for k in range(i)] + \
                           [matrix[j][i] + shadow_matrix[j + 1][i]] + \
                           [cost[k] - cost[i] + matrix[j][i] +
                            shadow_matrix[j + 1][k]for k in range(i + 1, rows)]

                shadow_matrix[j][i] += min(possible)

    return min(shadow_matrix[0])
