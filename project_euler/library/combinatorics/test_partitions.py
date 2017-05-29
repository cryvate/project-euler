from .partitions import partitions, Partitions, GeneratePartitions


def test_partitions() -> None:
    assert partitions(5) == 7
    assert partitions(5) == 7


def test_partitions_class() -> None:
    partitions_class = Partitions([2, 3, 5, 7])

    assert partitions_class[10] == 5


def test_generate_partitions() -> None:
    generate_partitions = GeneratePartitions()

    expected = [[1, 1, 1], [2, 1], [3]]

    assert len(expected) == len(generate_partitions(3))

    for partition in generate_partitions(3):
        assert partition in expected

    assert len(generate_partitions(10)) == partitions(10)
