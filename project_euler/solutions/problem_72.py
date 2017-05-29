from ..library.number_theory.stern_brocot_tree import size_stern_brocot_tree


def solve(bound: int=1_000_000) -> int:
    return size_stern_brocot_tree(bound)
