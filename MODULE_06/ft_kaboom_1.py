
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
from alchemy.grimoire.dark_spellbook import dark_spell_record


result = dark_spell_record("Cursed", "frogs, dogs and logs")
print(f"Testing record light spell: {result}")
