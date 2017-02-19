from project_euler.library.series import fibonacci_series


def solve(bound: int=4_000_000) -> str:
    series = fibonacci_series()

    counter = 0

    for rabbits in series:
        if rabbits >= bound:
            break

        if rabbits % 2 == 0:
            counter += rabbits

    return str(counter)
