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

    def key_vertices(item: Tuple[Vertex, Optional[float]]) -> Tuple[bool, float]:
        value = item[1]

        return value is None, value
        # don't include vertex: they might not be sortable
        # build in sort is guaranteed stable Python sort is stable

    while not all(done.values()):
        vertex, cost = min(((vertex, cost) for vertex, cost in costs.items() if not done[vertex]), key=key_vertices)

        if vertex == target:
            return cost

        done[vertex] = True

        print(80 * 80 - sum(done.values()))

        for step in edges_index[vertex]:
            new_vertex = step[0]
            step_cost = 1 if len(step) == 1 else step[1]
            new_cost = cost + step_cost

            if costs[new_vertex] is None:
                costs[new_vertex] = new_cost
            else:
                costs[new_vertex] = min(costs[new_vertex], new_cost)

    return costs


# to add: full, to specific target, including target, negative (Floyd-Warshall)
