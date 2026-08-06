#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            print()
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            try:
                strategy1.act(c1)
                strategy2.act(c2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


print("Tournament 0 (basic)")
opponents0: list[tuple[CreatureFactory, BattleStrategy]] = [
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
]
compr_1 = [
    (type(f).__name__ + '+' + type(s).__name__.replace('Strategy', ''))
    for f, s in opponents0
    ]
print(f" {compr_1}")
battle(opponents0)

print()

print("Tournament 1 (error)")
opponents1: list[tuple[CreatureFactory, BattleStrategy]] = [
    (FlameFactory(), AggressiveStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
]
compr_2 = [
    (type(f).__name__ + '+' + type(s).__name__.replace('Strategy', ''))
    for f, s in opponents1
    ]
print(f" {compr_2}")
battle(opponents1)

print()


print("Tournament 2 (multiple)")
opponents2: list[tuple[CreatureFactory, BattleStrategy]] = [
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy()),
]
compr_3 = [
    (type(f).__name__ + '+' + type(s).__name__.replace('Strategy', ''))
    for f, s in opponents2
    ]
print(f" {compr_3}")
battle(opponents2)
