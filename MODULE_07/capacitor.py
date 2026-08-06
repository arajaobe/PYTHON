#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import Sproutling, Bloomelle, Shiftling, Morphagon


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()

    print(" base:")
    base1: Sproutling = heal_factory.create_base()
    print(base1.describe())
    print(base1.attack())
    print(base1.heal())

    print(" evolved:")
    evolved1: Bloomelle = heal_factory.create_evolved()
    print(evolved1.describe())
    print(evolved1.attack())
    print(evolved1.heal())

    print()
    print("Testing Creature with transform capability")
    transform_factory = TransformCreatureFactory()

    print(" base:")
    base: Shiftling = transform_factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    evolved: Morphagon = transform_factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
