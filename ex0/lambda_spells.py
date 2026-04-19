# def artifact_sorter(artifacts: list[dict]) -> list[dict]
# def power_filter(mages: list[dict], min_power: int) -> list[dict]
# def spell_transformer(spells: list[str]) -> list[str]
# def mage_stats(mages: list[dict]) -> dict

import random
from typing import List, Dict, Any

MAGE_NAMES = [
    "Alex",
    "Jordan",
    "Riley",
    "Casey",
    "Morgan",
    "Sage",
    "River",
    "Phoenix",
    "Ember",
    "Storm",
    "Luna",
    "Nova",
    "Zara",
    "Kai",
    "Rowan",
    "Ash"]

ELEMENTS = [
    "fire",
    "ice",
    "lightning",
    "earth",
    "wind",
    "water",
    "light",
    "shadow"]

SPELL_NAMES = [
        "fireball", "heal", "shield", "lightning", "freeze", "earthquake",
        "tornado", "tsunami", "flash", "darkness", "meteor", "blizzard"
    ]

ARTIFACT_NAMES = [
    "Crystal Orb",
    "Fire Staff",
    "Ice Wand",
    "Lightning Rod",
    "Earth Shield",
    "Wind Cloak",
    "Water Chalice",
    "Shadow Blade",
    "Light Prism",
    "Storm Crown"]

ARTIFACT_TYPES = ["weapon", "focus", "armor", "accessory", "relic"]

ENCHANTMENT_TYPES = [
    "Flaming",
    "Frozen",
    "Shocking",
    "Earthen",
    "Windy",
    "Flowing",
    "Radiant",
    "Dark"]


def generate_mages(count: int = 5) -> List[Dict[str, Any]]:
    """Generate a list of mages with random attributes."""
    mages = []
    for _ in range(count):
        mage = {
            'name': random.choice(MAGE_NAMES),
            'power': random.randint(40, 100),
            'element': random.choice(ELEMENTS)
        }
        mages.append(mage)
    return mages


def generate_artifacts(count: int = 5) -> List[Dict[str, Any]]:
    """Generate a list of magical artifacts."""
    artifacts = []
    for _ in range(count):
        artifact = {
            'name': random.choice(ARTIFACT_NAMES),
            'power': random.randint(60, 120),
            'type': random.choice(ARTIFACT_TYPES)
        }
        artifacts.append(artifact)
    return artifacts


def generate_spells(count: int = 6) -> List[str]:
        """Generate a list of spell names."""
        return random.sample(SPELL_NAMES, min(count, len(SPELL_NAMES)))


def generate_spell_powers(count: int = 5) -> List[int]:
    """Generate a list of spell power values."""
    return [random.randint(10, 50) for _ in range(count)]


def generate_enchantment_items(count: int = 5) -> List[str]:
    """Generate a list of items to be enchanted."""
    items = [
        "Sword",
        "Shield",
        "Staff",
        "Wand",
        "Armor",
        "Ring",
        "Amulet",
        "Cloak"]
    return random.sample(items, min(count, len(items)))



artifact_sorter = lambda artifacts: sorted(artifacts, key=lambda artifact:
                                           artifact["power"], reverse=True)

mage_stats = lambda x: {
    "max_power": max(x),
    "min_power": min(x),
    "avg_power": sum(x)/len(x)
    } if x else {
    "max_power": 0,
    "min_power": 0,
    "avg_power": 0
    }


def main() -> None:
    print("Testing artifact sorter...")
    lista = generate_artifacts(4)
    print(f" Original: {lista}")
    lista = artifact_sorter(lista)
    print(f" Sorted:  {lista}")
    print()

    print("Testing power filter...")
    min_power = 50
    mages = generate_mages(4)
    power_filter = list(filter(lambda mage: mage["power"] < min_power,   mages))
    print(f" Original: {mages}")
    print(f" Filtered: {power_filter}")
    print()

    print("Testing spell transformer...")
    spells = generate_spells()
    print(f" Original {spells}")
    spell_transformer = list(map(lambda x: "*" + x + "*", spells))
    print(f" Transformed { spell_transformer}")
    print()

    print("Testing Merge Stats...")
    data = generate_spell_powers()
    print(f" Original {data}")

    res = mage_stats(data)
    print(f"Stats: {res}")


if __name__ == "__main__":
    main()
