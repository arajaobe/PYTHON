#!/usr/bin/env python3

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
            artifacts,
            key=lambda artifact: artifact["power"],
            reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    min_value = min(mages, key=lambda mage: mage["power"])
    max_value = max(mages, key=lambda mage: mage["power"])
    average = round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages), 2)
    return {
            "max_power": max_value["power"],
            "min_power": min_value["power"],
            "avg_power": average}


if __name__ == "__main__":
    artifacts: list[dict[str, Any]] = [{'name': 'Ice Wand',
                                        'power': 114,
                                        'type': 'relic'},
                                       {'name': 'Light prism',
                                        'power': 92,
                                        'type': 'armor'},
                                       {'name': 'Water Chalice',
                                        'power': 88,
                                        'type': "armor"},
                                       {'name': 'Fire Staff',
                                        'power': 99,
                                        'type': 'armor'}]

    mages: list[dict[str, Any]] = [{'name': 'Alex',
                                    'power': 93,
                                    'element': 'shadow'},
                                   {'name': 'Luna',
                                    'power': 65,
                                    'element': 'water'},
                                   {'name': 'Morgan',
                                    'power': 69,
                                    'element': 'fire'},
                                   {'name': 'Sage',
                                    'power': 51,
                                    'element': 'light'},
                                   {'name': 'Riley',
                                    'power': 50,
                                    'element': 'fire'}]

    spells = ['heal', 'fireball', 'earthquake', 'shield']
    try:
        print("Testing artifact sorter...")
        sort = artifact_sorter(artifacts)
        i = 0
        for i in range(len(sort) - 1):
            print(
                    f"{sort[i]['name']} ({sort[i]['power']} power) "
                    f"comes before "
                    f"{sort[i + 1]['name']} ({sort[i + 1]['power']} power)")
        print()
        print("Testing power filter...")
        power = power_filter(mages, 50)
        for mage in power:
            print(f"{mage['name']} - "
                  f"{mage['power']} power-"
                  f"{mage['element']}")
        print()
        print("Testing spell transformer...")
        spell = spell_transformer(spells)
        print(*spell)
        print()
        print("Testing mage stats...")
        stats = mage_stats(mages)
        print(f"Maximum power: {stats['max_power']}")
        print(f"Minimum power: {stats['min_power']}")
        print(f"Average power: {stats['avg_power']}")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")