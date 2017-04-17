from ..framework.load_file import load_file


def solve(name: str='matrix.txt', relative: bool=True):
    matrix_raw = load_file(81, name, relative)

    matrix = [[int(n) for n in line.split(',')]
              for line in matrix_raw.split('\n') if line]

    shadow_matrix = [[0 for _ in line] for line in matrix]
    shadow_matrix[0][0] = matrix[0][0]

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows + columns - 1):
        for j in range(i + 1):
            x = j
            y = i - j

            if x >= rows or y < 0:  # will only get worse: break
                break

            if x < 0 or y >= columns:  # will fix itself: continue
                continue

            shadow_matrix[x][y] = matrix[x][y]

            if x == 0 and y == 0:
                pass
            elif x == 0:
                shadow_matrix[x][y] += shadow_matrix[x][y - 1]
            elif y == 0:
                shadow_matrix[x][y] += shadow_matrix[x - 1][y]
            else:
                shadow_matrix[x][y] += min(shadow_matrix[x][y - 1],
                                           shadow_matrix[x - 1][y])

    return shadow_matrix[-1][-1]
