from typing import Any, List, Tuple

from ..framework.load_file import load_file
from ..library.optimization.dijkstra import source_target_dijkstra_cost

Coordinate = Tuple[int, int]
Edge = Tuple[Coordinate, Coordinate, Any]
Step = Tuple[Edge, Edge, Any]


def string_to_matrix(matrix_string: str) -> List[List[Any]]:
    return [[int(n) for n in line.split(',')]
            for line in matrix_string.split('\n') if line]


def matrix_steps_to_vertices_edges(matrix: List[List[Any]],
                                   steps: List[Step],
                                   sources: List[Coordinate],
                                   drains: List[Coordinate]) -> \
    Tuple[List[Coordinate], Edge]:
    rows = len(matrix)
    columns = len(matrix[0])

    source = (-1, 0)
    drain = (0, -1)

    vertices = [source] + \
               [(i, j) for i in range(rows) for j in range(columns)] + \
               [drain]

    edges = []

    for s in sources:
        edges.append((source, s, 0))

    for d in drains:
        edges.append((d, drain, matrix[d[0]][d[1]]))

    for i in range(rows):
        for j in range(columns):
            cost = matrix[i][j]

            for step_x, step_y in steps:
                x = i + step_x
                y = j + step_y

                if 0 <= x < rows and 0 <= y < columns:
                    edges.append(((i, j), (x, y), cost))

    return vertices, edges


def solve(name: str='matrix.txt',
          relative: bool=True,
          steps: List[Step]=((0, 1), (1, 0)),
          sources: List[Coordinate]=((0, 0), ),
          drains: List[Coordinate]=((-1, -1), )):
    matrix_string = load_file('81_82_83', name, relative)
    matrix = string_to_matrix(matrix_string)

    rows = len(matrix)
    columns = len(matrix[0])

    sources = [(i % rows, j % columns) for i, j in sources]
    drains = [(i % rows, j % columns) for i, j in drains]

    vertices, edges = matrix_steps_to_vertices_edges(matrix,
                                                     steps,
                                                     sources,
                                                     drains)

    result = source_target_dijkstra_cost(vertices, edges, (-1, 0), (0, -1))

    return result
