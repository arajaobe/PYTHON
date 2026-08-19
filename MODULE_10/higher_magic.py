#!/usr/bin/env python3

from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def conditional_test(target: str, power: int) -> bool:
    return power >= 20


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Arguments must be callable")

    def combined(target: str, power: int) -> tuple[str, str]:
        s1 = spell1(target, power)
        s2 = spell2(target, power)
        return (s1, s2)
    return combined


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:
    if not callable(base_spell):
        raise TypeError("base_spell must be callable")

    def amplified(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)
    return amplified


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    if not callable(condition) or not callable(spell):
        raise TypeError("Arguments must be callable")

    def caster(target: str, power: int) -> str:
        if condition(target, power) is True:
            return spell(target, power)
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    for spell in spells:
        if not callable(spell):
            raise TypeError("All elements in spells must be callable.")

    def sequence(target: str, power: int) -> list[str]:
        result = []
        for spell in spells:
            element = spell(target, power)
            result.append(element)
        return result
    return sequence


if __name__ == "__main__":
    try:
        print("Testing spell combiner ...")
        combined = spell_combiner(fireball, heal)
        combined_1, combined_2 = combined('Dragon', 10)
        print(f"Combined spell result: {combined_1}, {combined_2}")

        print("\nTesting power amplifier ...")
        mega_fireball = power_amplifier(fireball, 3)
        print("Original:")
        print(fireball("Dragon", 10))
        print("Amplified:")
        print(mega_fireball("Dragon", 10))

        print("\nTesting conditional caster ...")
        test_fireball = conditional_caster(conditional_test, fireball)
        print(test_fireball("Dragon", 10))
        print(test_fireball("Dragon", 25))

        print("\nTesting spell sequence ...")
        combo = spell_sequence([fireball, heal])
        results = combo("Dragon", 15)
        for result in results:
            print(f"- {result}")
    except Exception as e:
        print(f"Error: {e}")
