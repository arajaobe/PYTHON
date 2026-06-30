#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:03:50 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/02 13:09:53 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def grow(self, amount: float = 0.8) -> None:
        self.height += amount

    def age_one_day(self) -> None:
        self.age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> str:
        base = super().show()
        if self.bloomed:
            return ((f"{base}\nColor: {self.color}\n{self.name}"
                    f" is blooming beautifully!"))
        else:
            return ((f"{base}\nColor: {self.color}\n{self.name}"
                    f" has not bloomed yet"))


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        return (f"Tree {self.name} now produces a shade of {self.height:.1f}cm"
                f" long and {self.trunk_diameter:.1f}cm wide")

    def show(self) -> str:
        base = super().show()
        return f"{base}\nTrunk diameter: {self.trunk_diameter:.1f}cm"


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self.nutritional_value += 1

    def show(self) -> str:
        base = super().show()
        return (f"{base}\nHarvest season: {self.harvest_season}\n"
                f"Nutritional value: {self.nutritional_value}")


def flower_state(plants: Plant, result: bool = False) -> None:
    if result:
        print("[asking the rose to bloom]")
    print(plants.show())


def display_plants(flower_plant: Flower, tree_plant: Tree,
                   vegetable_plant: Vegetable) -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower_state(flower_plant)
    result = True
    flower_plant.bloom()
    flower_state(flower_plant, result)
    print("")
    print("=== Tree")
    print(tree_plant.show())
    print("[asking the oak to produce shade]")
    print(tree_plant.produce_shade())
    print("")
    print("=== Vegetable")
    print(vegetable_plant.show())
    print("[make tomato grow and age for 20 days]")
    for _ in range(1, 21):
        vegetable_plant.grow()
        vegetable_plant.age_one_day()
    print(vegetable_plant.show())


def main() -> None:
    plant1 = Flower("Rose", 30, 25, "red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant3 = Vegetable("Tomato", 5.0, 10, "April")
    display_plants(plant1, plant2, plant3)


if __name__ == "__main__":
    main()
