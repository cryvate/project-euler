from .partitions import partitions, Partitions


def test_partitions() -> None:
    assert partitions(5) == 7
    assert partitions(5) == 7


def test_partitions_class() -> None:
    partitions_class = Partitions([2, 3, 5, 7])

    assert partitions_class[10] == 5
