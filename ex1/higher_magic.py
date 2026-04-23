from collections.abc import Callable
from typing import Any
import random

SPELL_NAMES = [
    "fireball", "heal", "shield", "lightning", "freeze", "earthquake",
    "tornado", "tsunami", "flash", "darkness", "meteor", "blizzard"
]


def condition_function_true(*args: Any, **kwargs: Any) -> bool:
    return True


def condition_function_false(*args: Any, **kwargs: Any) -> bool:
    return False


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def hit(target: str, power: int) -> str:
    return f"Hit damages {target} for {power} HP"


def explosion(target: str, power: int) -> str:
    return f"Explosion damages {target} for {power} HP"


def main() -> None:
    combined = spell_combiner(heal, hit)
    print(combined("Orc", 30))

    amplifier = power_amplifier(heal, 5)
    print(amplifier("Orc", 30))
    conditional = conditional_caster(condition_function_true, heal)
    print(conditional("Orc", 30))
    conditional2 = conditional_caster(condition_function_false, heal)
    print(conditional2("Orc", 30))

    spells: list[Callable] = [heal, hit, explosion]
    spell_iterator = spell_sequence(spells)
    print(spell_iterator("Orc", 30))


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_iterator(*args: Any, **kwargs: Any) -> list[str]:
        result: list[str] = []
        for spell in spells:
            result.append(spell(*args, **kwargs))
        return result
    return spell_iterator


def multiplier(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def generate_spells(count: int = 6) -> list[str]:
    """Generate a list of spell names."""
    return random.sample(SPELL_NAMES, min(count, len(SPELL_NAMES)))


if __name__ == "__main__":
    main()
