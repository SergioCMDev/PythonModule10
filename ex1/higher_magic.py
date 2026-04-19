from collections.abc import Callable


def main() -> None:
	pass

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable
def power_amplifier(base_spell: Callable, multiplier: int) -> Callable
def conditional_caster(condition: Callable, spell: Callable) -> Callable
def spell_sequence(spells: list[Callable]) -> Callable


def spell(target: str, power: int) -> str:
	pass

def heal(target: str, power: int) -> str:
	return f"Heal restores {target} for {power} HP"

if __name__ == "__main__":
    main()
