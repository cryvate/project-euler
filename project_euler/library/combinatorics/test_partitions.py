from project_euler.library.combinatorics.partitions import partitions


def test_partitions() -> None:
    assert partitions(5) == 7

    assert partitions(10, [2, 3, 5, 7]) == 5
