from typing import Dict, Hashable, Iterable, Optional, Tuple, Union

Vertex = Hashable
Edge = Union[Tuple[Vertex, Vertex, float], Tuple[Vertex, Vertex]]


def source_target_dijkstra_cost(vertices: Iterable[Vertex],
                                edges: Iterable[Edge],
                                source: Vertex,
                                target: Vertex) -> Dict[Vertex, float]:
    vertices = list(vertices)

    edges_index = {vertex: [] for vertex in vertices}

    for edge in edges:
        edges_index[edge[0]].append(edge[1:])

    costs = {vertex: None for vertex in vertices}
    costs[source] = 0

    done = {vertex: False for vertex in vertices}

    while done:
        minimal_cost = None

        # own minimal method written, because built-in is slow
        for vertex, cost in costs.items():
            if cost is not None:
                if minimal_cost is None or cost < minimal_cost:
                    minimal_cost = cost
                    minimal_vertex = vertex

        vertex, cost = minimal_vertex, minimal_cost

        if vertex == target:
            return cost

        done.pop(vertex)
        costs.pop(vertex)

        for step in edges_index[vertex]:
            new_vertex = step[0]
            step_cost = 1 if len(step) == 1 else step[1]
            new_cost = cost + step_cost

            try:
                if costs[new_vertex] is None:
                    costs[new_vertex] = new_cost
                else:
                    costs[new_vertex] = min(costs[new_vertex], new_cost)
            except KeyError:
                pass  # vertex is already done

# to add: if target isn't reached, make sure to throw exception (this is when
# minimal cost is not set as PyCharm suggests.
# to add: full, to specific target, including target, negative (Floyd-Warshall)
