from collections import Counter
from time import time
from typing import List, Optional, Tuple

from ..framework.load_file import load_file
from ..library.base import list_to_number

Sudoku = List[List[int]]
spec = '{:6.6f}'


class SetNoZero(set):
    def add(self, x) -> None:
        if x != 0:
            super().add(x)

    def __sub__(self, other) -> None:
        return SetNoZero(super().__sub__(other))


digits = SetNoZero(range(1, 10))


def sstr(input: Sudoku) -> str:
    output = ''
    for i in range(9):
        for j in range(9):
            output += str(input[i][j])
            if j % 3 == 2:
                output += ' '

        output += '\n'
        if i % 3 == 2:
            output += '\n'

    return output.strip('\n')


def least(input: Sudoku) -> Optional[Tuple[int, int]]:
    for i in range(9):
        for j in range(9):
            if input[i][j] == 0:
                return i, j

    return None


def constraint_solve_sudoku(input: Sudoku) -> Tuple[bool, Optional[Sudoku]]:
    # these are kept up to date as parts filled in
    lines = []
    columns = []
    boxes = []

    for i in range(9):
        line = SetNoZero()
        column = SetNoZero()

        for j in range(9):
            line.add(input[i][j])
            column.add(input[j][i])

        lines.append(digits - line)
        columns.append(digits - column)

    for i in range(3):
        boxes.append([])
        for j in range(3):
            box = SetNoZero()
            for k in range(3):
                for l in range(3):
                    box.add(input[i * 3 + k][j * 3 + l])
            boxes[i].append(digits - box)

    flag = True

    while least(input):
        if not flag:
            i, j = least(input)

            # allowed guaranteed to exist, because the flag starts as true.
            for value in allowed[i][j]:  # noqa: F821
                new_input = [[input[i][j] for j in range(9)] for i in range(9)]
                new_input[i][j] = value

                done, solution = constraint_solve_sudoku(new_input)

                if done:
                    return True, solution

            return False, None

        flag = False

        allowed = []

        for i in range(9):
            line = lines[i]
            allowed.append([])
            for j in range(9):
                if input[i][j] != 0:
                    allowed[i].append(None)
                else:
                    column = columns[j]
                    box = boxes[i // 3][j // 3]

                    allowed[i].append({d for d in digits if
                                       d in line and d in column and d in box})

        updates = []

        for i in range(9):
            for j in range(9):
                if allowed[i][j] and len(allowed[i][j]) == 1:
                    updates.append((i, j, list(allowed[i][j])[0]))

        for i in range(9):
            counter = Counter()

            for j in range(9):
                if allowed[i][j]:
                    counter.update(allowed[i][j])

            for value, count in counter.items():
                if count == 1:
                    for j in range(9):
                        if allowed[i][j] and value in allowed[i][j]:
                            updates.append((i, j, value))

        for i in range(9):
            counter = Counter()

            for j in range(9):
                if allowed[j][i]:
                    counter.update(allowed[j][i])

            for value, count in counter.items():
                if count == 1:
                    for j in range(9):
                        if allowed[j][i] and value in allowed[j][i]:
                            updates.append((j, i, value))

        for i in range(3):
            for j in range(3):
                counter = Counter()

                for k in range(3):
                    for l in range(3):
                        allowedness = allowed[i * 3 + k][j * 3 + l]
                        if allowedness:
                            counter.update(allowed[i * 3 + k][j * 3 + l])

                for value, count in counter.items():
                    if count == 1:
                        for k in range(3):
                            for l in range(3):
                                allowedness = allowed[i * 3 + k][j * 3 + l]
                                if allowedness and value in allowedness:
                                    updates.append((i * 3 + k, j * 3 + l,
                                                    value))

        if updates:
            flag = True
        updates = set(updates)

        for i, j, value in updates:
            input[i][j] = value

            allowed[i][j] = None
            try:
                lines[i].remove(value)
                columns[j].remove(value)
                boxes[i // 3][j // 3].remove(value)
            except KeyError:  # means that this sudoku is inconsistent
                return False, None

    return True, input


def solve(name: str='sudoku.txt', relative: bool=True) -> int:
    raw = load_file(96, name, relative)

    grids_str = [[line for line in grid.split('\n')[1:] if line]
                 for grid in raw.split('Grid') if grid]
    grids = [[[int(d) for d in line] for line in grid] for grid in grids_str]

    accumulate = 0

    for i, grid in enumerate(grids):
        print('={:>2}th grid='.format(i))

        start = time()
        _, solution = constraint_solve_sudoku(grid)
        spent = time() - start

        print(sstr(solution))
        accumulate += list_to_number(solution[0][0:3])
        print(f'({spec.format(spent)}s)')

    return accumulate
