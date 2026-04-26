from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter: int = 1

    def counting() -> int:
        nonlocal counter
        counter += 1
        return counter

    return counting


def spell_accumulator(initial_power: int) -> Callable:
    power: int = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal power
        power += power_to_add
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    enchantment_base: str = enchantment_type

    def applicator(item_name: str) -> str:
        nonlocal enchantment_base

        return f"{enchantment_base} {item_name}"

    return applicator


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        nonlocal memory
        memory[key] = value

    def recall(key: str) -> Any:
        nonlocal memory
        return memory[key] if key in memory.keys() else "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage_counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a 1: {counter_a()}")
    print(f"counter_a 2: {counter_a()}")
    print(f"counter_b 1: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    base: int = 100
    added_1: int = 20
    added_2: int = 30
    accumulator = spell_accumulator(base)
    print(f"Base {base}, add {added_1}: {accumulator(added_1)}")
    print(f"Base {base}, add {added_2}: {accumulator(added_2)}")
    print()

    print("Testing enchantment factory...")
    factory_flaming = enchantment_factory("Flaming")
    factory_frozen = enchantment_factory("Frozen")
    print(factory_flaming("Sword"))
    print(factory_frozen("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    key_to_store: str = "secret"
    vault["store"]("secret", "42")
    print("Store 'secret' = 42")
    print(f"Recall '{key_to_store}': {vault["recall"](key_to_store)}")
    key_to_store = "unknown"

    print(f"Recall '{key_to_store}': {vault["recall"](key_to_store)}")


if __name__ == "__main__":
    main()
