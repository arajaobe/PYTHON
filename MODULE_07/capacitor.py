
from ex1 import HealingCreatureFactory , TransformCreatureFactory


print("Testing Creature with healing capability")
heal_factory = HealingCreatureFactory()

print(" base:")
base = heal_factory.create_base()
print(base.describe())
print(base.attack())
print(base.heal())

print(" evolved:")
evolved = heal_factory.create_evolved()
print(evolved.describe())
print(evolved.attack())
print(evolved.heal())


print()
print("Testing Creature with transform capability")
transform_factory = TransformCreatureFactory()

print(" base:")
base = transform_factory.create_base()
print(base.describe())
print(base.attack())
print(base.transform())
print(base.attack())
print(base.revert())

print(" evolved:")
evolved = transform_factory.create_evolved()
print(evolved.describe())
print(evolved.attack())
print(evolved.transform())
print(evolved.attack())
print(evolved.revert())
