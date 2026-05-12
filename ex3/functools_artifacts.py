from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from typing import Any


allowed_operations = ("add", "multiply", "max", "min")


def enachment(power: int, element: str, target: str) -> str:
    return f"power {power} element {element} to target {target}"


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
    power: int = 20
    element: str = "Fire"
    target: str = "Orc"
    power_res = partial(base_enchantment, power=power)
    element_res = partial(base_enchantment, element=element)
    target_res = partial(base_enchantment, target=target)
    return {"power": power_res, "element": element_res, "target": target_res}


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if (n <= 1):
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(spell: Any) -> str:
    return (f"unknwon spell type {spell}")


@spell_dispatcher.register(int)
def _ (arg: int) -> str:
    return (f"Damage spell: {arg} damage")


@spell_dispatcher.register(str)
def _ (arg: str) -> str:
    return (f"Enachment: {arg}")


@spell_dispatcher.register(list)
def _ (arg: list[Any]) -> str:
    return (f"Multi-cast: {len(arg)} spells")


def main() -> None:
    lista: list[int] = [1, 2, 4, 5, 6]
    print("Test spell reducer")
    print(f"Sum {spell_reducer(lista, 'add')}")
    print(f"Product {spell_reducer(lista, 'multiply')}")
    print(f"Max {spell_reducer(lista, 'max')}")
    print(f"Min {spell_reducer(lista, 'min')}")
    print()
    print("Test partial enchanter")
    ench = partial_enchanter(enachment)
    print(ench["power"](element="Fire", target="Orc"))

    print("Testing memoized fibonacci...")
    print(memoized_fibonacci(5))

    print("Testing spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    spells: list[str] = ["heal", "fireball", "poison"]
    print(spell_dispatcher(spells))
    print(spell_dispatcher(4.9))


if __name__ == "__main__":
    main()
