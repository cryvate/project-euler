from itertools import count

from ..library.base import list_to_number

operators = (float.__add__, float.__mul__, float.__sub__, float.__truediv__)


def possibilities(a, b, c, d):
    vars = {a * 1.0, b * 1.0, c * 1.0, d * 1.0}
    results = []
    for v1 in vars:
        for v2 in vars - {v1}:
            for v3 in vars - {v1, v2}:
                v4 = list((vars - {v1, v2, v3}))[0]
                for op1 in operators:
                    for op2 in operators:
                        for op3 in operators:
                            result1 = op3(op2(op1(v1, v2), v3), v4)
                            result2 = op3(op1(v1, v2), op2(v3, v4))

                            if result1 > 0 and int(result1) == result1:
                                results.append(int(result1))
                            if result2 > 0 and int(result2) == result2:
                                results.append(int(result2))

    return sorted(set(results))


def solve(bound: int=10) -> int:
    bound = bound

    max_result = 0
    representation = None

    for a in range(1, bound):
        for b in range(a + 1, bound):
            for c in range(b + 1, bound):
                for d in range(c + 1, bound):
                    expressible = possibilities(a, b, c, d)

                    for result in count(1):
                        if expressible[result - 1] != result:
                            break

                    if result > max_result:
                        max_result = result
                        representation = list_to_number((a, b, c, d))

    return representation
