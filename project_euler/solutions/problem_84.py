from enum import Enum

from typing import Any, List

import numpy as np

class Square(Enum):
    Otherwise = 0
    GoToJail = 1
    CommunityChest = 2
    Chance = 3
    Railroad = 4
    Utility = 5

BOARD = [Square.Otherwise for i in range(40)]

for i in [2, 17, 33]:
    BOARD[i] = Square.CommunityChest

for i in [7, 22, 36]:
    BOARD[i] = Square.Chance

for i in [5, 15, 25, 35]:
    BOARD[i] = Square.Railroad

for i in [12, 28]:
    BOARD[i] = Square.Utility

BOARD[10] = Square.GoToJail


def flatten(l: List[List[Any]]) -> List[Any]:
    return [item for sublist in l for item in sublist]


def solve(sides: int=4,
          board: List[Square]=BOARD,
          jail_position: int=10,
          doubles: int=3) -> str:
    length = len(board)
    states = [[(position, square, i) for position, square in enumerate(board)]
              for i in range(doubles)]

    actions = []

    for position, square in enumerate(board):
        transition = [0 for i in range(length)]
        if square in (Square.Otherwise, Square.Railroad, Square.Utility):
            pass
        elif square == Square.GoToJail:
            transition[jail_position] = 1
        else:
            size = 16
            positions = []
            if square == Square.CommunityChest:
                positions += [0, jail_position]
            if square == Square.Chance:
                positions += [0,   # home
                              11,  # c1
                              25,  # e3
                              39,  # h2
                              5,   # r1
                              jail_position,
                              (position - 3) % length]

                next_r = (position + (board[position:] + board[:position])
                          .index(Square.Railroad)) % length
                next_u = (position + (board[position:] + board[:position])
                          .index(Square.Utility)) % length

                positions += [next_r,
                              next_r,  # because in cards twice
                              next_u]

            for i in positions:
                transition[i] += 1 / size

        transition[position] += 1 - sum(transition)
        actions.append(transition)

    dice_factor = sides ** -2
    dice_probs = {}

    for total in range(2 * sides):
        for double in [False, True]:
            dice_probs[(total + 2, double)] = 0

    for i in range(sides):
        for j in range(sides):
            dice_probs[(i + j + 2, i == j)] += 1

    for key in dice_probs:
            dice_probs[key] *= dice_factor

    assert sum(dice_probs.values()) == 1

    transitions = [[None for _ in range(length)] for _ in range(doubles)]
    for doubles_already in range(doubles):
        transitions.append([])

        for position in range(length):
            transition = [[0 for _ in range(length)] for _ in range(doubles)]

            for total, double in dice_probs:
                local_transition = [0 for i in range(length)]

                doubles_new = doubles_already + 1 if double else 0

                if doubles_new == doubles:
                    doubles_new %= doubles
                    local_transition[jail_position] = 1
                else:
                    local_transition = actions[(position + total) % length]

                for i in range(length):
                    transition[doubles_new][i] += local_transition[i]

            for i in range(doubles):
                for j in range(length):
                    transition[i][j] *= dice_factor

            assert sum(sum(b) for b in transition) == 1

            transitions[doubles_already][position] = transition

    transitions_flat = [[flatten(transitions[i][j]) for j in range(length)] for i in range(doubles)]
    transitions_matrix = flatten(transitions_flat)

    transitions_np = np.matrix(transitions_matrix)

    transitions_np **= 50

    steady = transitions_np[0,:].tolist()[0]
    steady_no_doubles = [[0, i] for i in range(length)]
    #print(transitions_np[0,:] - transitions_np[-1,:])

    for position, value in enumerate(steady):
        steady_no_doubles[position % length][0] -= value

    print(sorted(steady_no_doubles)[0:20])

    return ''.join(str(position) for _, position in sorted(steady_no_doubles)[0:3])
