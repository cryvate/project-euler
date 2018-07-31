from ..framework.load_file import load_file


def crossproduct(p, q):
    return p[0] * q[1] - p[1] * q[0]


def subtract(p, q):
    return [x - y for x, y in zip(p, q)]


def same_side(p, q, a, b):
    ab = subtract(a, b)
    cp1 = crossproduct(ab, subtract(p, a))
    cp2 = crossproduct(ab, subtract(q, a))
    if cp1 * cp2 >= 0:
        return True
    else:
        return False


def solve(name: str='triangles.txt', relative: bool=True) -> int:
    raw = load_file(102, name, relative)

    triangles = []

    for line in raw.split('\n'):
        if not line:
            continue

        coordinates = [int(x) for x in line.split(',')]
        vectors = list(zip(coordinates[0::2], coordinates[1::2], [0] * 3))

        triangles.append(vectors)

    total = 0
    origin = [0, 0, 0]

    for i in triangles:
        if (
            same_side(origin, i[0], i[1], i[2]) and
            same_side(origin, i[1], i[0], i[2]) and
            same_side(origin, i[2], i[0], i[1])
        ):
            total += 1

    return total
