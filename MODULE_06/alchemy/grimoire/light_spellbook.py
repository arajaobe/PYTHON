
def light_spell_alowed_ingredients() -> list[str]:
    return["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} - {result})"
