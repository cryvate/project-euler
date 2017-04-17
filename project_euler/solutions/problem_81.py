from ..framework.load_file import load_file


def solve(name: str='matrix.txt', relative: bool=True):
    matrix_raw = load_file(81, name, relative)

    matrix = [[int(n) for n in line.split(',')]
              for line in matrix_raw.split('\n') if line]

    shadow_matrix = [[0 for _ in line] for line in matrix]

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows + columns - 1):
        for j in range(i + 1):
            x = rows - 1 - j
            y = columns - 1 - i + j

            if x < 0 or y >= columns:  # will only get worse: break
                break

            if x >= rows or y < 0:  # will fix itself: continue
                continue

            shadow_matrix[x][y] = matrix[x][y]

            if x == rows - 1 and y == columns - 1:
                pass
            elif x == rows - 1:
                shadow_matrix[x][y] += shadow_matrix[x][y + 1]
            elif y == columns - 1:
                shadow_matrix[x][y] += shadow_matrix[x + 1][y]
            else:
                shadow_matrix[x][y] += min(shadow_matrix[x][y + 1],
                                           shadow_matrix[x + 1][y])

    return shadow_matrix[0][0]
