from .dijkstra import source_target_dijkstra_cost
from ...solutions.problem_81 import matrix_steps_to_vertices_edges


def test_dijkstra() -> None:
    matrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]

    rows = len(matrix)
    columns = len(matrix[0])

    sources = [(0, 0)]
    drains = [(-1 % rows, -1 % columns)]
    steps = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    v, e = matrix_steps_to_vertices_edges(matrix, steps, sources, drains)

    source_target_dijkstra_cost(v, e, (-1, 0), (0, -1))
