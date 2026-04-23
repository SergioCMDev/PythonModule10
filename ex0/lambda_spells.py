from data_generator import FuncMageDataGenerator


artifact_sorter = lambda artifacts: sorted(artifacts,  # noqa: E731
                                           key=lambda artifact:
                                           artifact["power"], reverse=True)


mage_stats = lambda x: {  # noqa: E731
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
    lista = FuncMageDataGenerator.generate_artifacts(4)
    print(f" Original: {lista}")
    lista = artifact_sorter(lista)
    print(f" Sorted:  {lista}")
    print()

    print("Testing power filter...")
    min_power = 50
    mages = FuncMageDataGenerator.generate_mages(4)
    power_filter = list(filter(lambda mage: mage["power"] < min_power, mages))
    print(f" Original: {mages}")
    print(f" Filtered: {power_filter}")
    print()

    print("Testing spell transformer...")
    spells = FuncMageDataGenerator.generate_spells()
    print(f" Original {spells}")
    spell_transformer = list(map(lambda x: "*" + x + "*", spells))
    print(f" Transformed {spell_transformer}")
    print()

    print("Testing Merge Stats...")
    data = FuncMageDataGenerator.generate_spell_powers()
    print(f" Original {data}")

    res = mage_stats(data)
    print(f"Stats: {res}")


if __name__ == "__main__":
    main()
