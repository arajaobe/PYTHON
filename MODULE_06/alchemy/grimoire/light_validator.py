
from alchemy.grimoire.light_spellbook import light_spell_alowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_alowed_ingredients()
    for item in allowed:
        if item.lower() in ingredients.lower():
            return "VALID"
    return "INVALID"