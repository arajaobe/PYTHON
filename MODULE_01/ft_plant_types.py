#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:03:50 by arajaobe            #+#    #+#            #
#   Updated: 2026/05/28 14:29:01 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height_cm: float, age_d: int):
        self.name = name
        self.height = height_cm
        self.age = age_d

    def show(self):
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def grow(self, amount: float = 0.8):
        self.height += amount

    def age_one_day(self):
        self.age += 1

class Flower(Plant):
    def __init__(self, name: str, height_cm: float, age_d: int, color: str):
        super().__init__(name, height_cm, age_d)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        base = super().show()
        if self.bloomed:
            return(f"{base}\nColor: {self.color}\n{self.name} is blooming beautifully!")
        else:
            return(f"{base}\nColor: {self.color}\n{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height_cm: float, age_d: int, trunk_diameter: float):
        super().__init__(name, height_cm, age_d)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return f"Tree {self.name} now produces a shade of {self.height:.1f}m long and {self.trunk_diameter:.1f}cm wide"

    def show(self):
        base = super().show()
        return f"{base}\nTrunk diameter: {self.trunk_diameter:.1f}cm"

class Vegetable(Plant):
    def __init__(self, name: str, height_cm: float, age_d: int, harvest_season: str):
        super().__init__(name, height_cm, age_d)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float = 2.1):
        super().grow(amount)
        self.nutritional_value += 1

    def show(self):
        base = super().show()
        return f"{base}\nHarvest season: {self.harvest_season}\nNutritional value: {self.nutritional_value}"


def flower_state(plants, result=False):
    if result:
        print("[asking the rose to bloom]")
    print(plants.show())

def display_plants(flower_plant, tree_plant, vegetable_plant):
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower_state(flower_plant)
    result = True
    flower_plant.bloom()
    flower_state(flower_plant, result)
    print("\n")
    print("=== Tree")
    print(tree_plant.show())
    print("[asking the oak to produce shade]")
    print(tree_plant.produce_shade())
    print("\n")
    print("=== Vegetable")
    print(vegetable_plant.show())
    print("[make tomato grow and age for 20 days]")
    for _ in range(1, 21):
        vegetable_plant.grow()
        vegetable_plant.age_one_day()
    print(vegetable_plant.show())

def main():
    plant1 = Flower("Rose", 30, 25, "Red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant3 = Vegetable("Tomato", 5.0, 10, "April")
    display_plants(plant1, plant2, plant3)

if __name__ == "__main__":
    main()
