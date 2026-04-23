from collections.abc import Callable
from functools import reduce
from typing import Any


allowed_operations = ("add", "multiply", "max", "min")


def spell_reducer(spells: list[int], operation: str) -> int:
    if (len(spells) == 0):
        return 0
    if (operation not in allowed_operations):
        return 0
    match operation:
        case "add":
            return reduce(lambda acc, x: acc + x, spells)
        case "multiply":
            return reduce(lambda acc, x: acc * x, spells)
        case "max":
            return reduce(lambda acc, x: acc if acc > x else x, spells)

        case "min":
            return reduce(lambda acc, x: acc if acc < x else x, spells)
        case _:
            return 0

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass

def memoized_fibonacci(n: int) -> int:
    pass

def spell_dispatcher() -> Callable[[Any], str]:
    pass


def main() -> None:
    lista: list[int] = [1, 2, 4, 5, 6]
    print(spell_reducer(lista, "add"))
    print(spell_reducer(lista, "multiply"))
    print(spell_reducer(lista, "max"))
    print(spell_reducer(lista, "min"))


if __name__ == "__main__":
    main()
