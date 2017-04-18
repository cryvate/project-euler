from enum import Enum

import numpy as np


class Square(Enum):
    Otherwise = 0
    GoToJail = 1
    CommunityChest = 2
    Chance = 3
    RailRoad = 4
    Utility = 5
    Jail = 6


def solve(sides: int=4) -> str:
    board = [Square.Otherwise for i in range(40)]
    length = len(board)
    jail_index = 10
    community_chests = [2, 17, 33]
    chance = [7, 22, 36]
    go_to_jail = [30]

    for i in community_chests:
        board[i] = Square.CommunityChest

    for i in chance:
        board[i] = Square.Chance

    for i in [5, 15, 25, 35]:
        board[i] = Square.RailRoad

    for i in [12, 28]:
        board[i] = Square.Utility

    for i in go_to_jail:
        board[i] = Square.GoToJail

    board[jail_index] = Square.Jail

    transitions_matrix = np.zeros((length, length))

    pdf = {total: 0 for total in range(6 * sides)}
    pdf[Square.Jail] = 0

    for i in range(sides):
        for j in range(sides):
            total1 = i + j + 2
            if i != j:
                pdf[total1] += sides ** -2
            else:
                for k in range(sides):
                    for m in range(sides):
                        total2 = total1 + k + m + 2
                        if k != m:
                            pdf[total2] += sides ** -4
                        else:
                            for n in range(sides):
                                for p in range(sides):
                                    total3 = total2 + n + p + 2
                                    if n != p:
                                        pdf[total3] += sides ** -6
                                    else:
                                        pdf[Square.Jail] += sides ** -6

    for position in range(length):
        for step, probability in pdf.items():
            if step == Square.Jail:
                step = jail_index

            transitions_matrix[position][(position + step) % length] += probability

    old = np.copy(transitions_matrix)

    for position in range(length):
        transition = transitions_matrix[position]

        for i in chance:
            probability = transition[i]

            transition[0] += probability * 1 / 16
            transition[jail_index] += probability * 1 / 16

            transition[i] -= probability * 2 / 16

        for i in community_chests:
            next_r = (position + (board[position:] + board[:position])
                      .index(Square.RailRoad)) % length
            next_u = (position + (board[position:] + board[:position])
                      .index(Square.Utility)) % length
            positions = [0,       # home
                         11,      # c1
                         24,      # e3
                         39,      # h2
                         5,       # r1
                         jail_index,
                         (position - 3) % length,
                         next_r,
                         next_r,  # because in cards twice
                         next_u]

            probability = transition[i]

            for j in positions:
                transition[j] += probability * 1 / 16

            transition[i] -= probability * 10 / 16

        for i in go_to_jail:
            transition[jail_index] += transition[i]
            transition[i] = 0

    transitions_matrix = np.matrix(transitions_matrix, copy=False)
    transitions_matrix **= 50

    stable = np.ndarray((length,), buffer=transitions_matrix[0])

    result = sorted((-value, pos) for pos, value in enumerate(stable))

    return ''.join(str(pos).zfill(2) for _, pos in sorted(result)[0:3])
