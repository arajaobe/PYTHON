#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 12:10:05 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/02 14:00:44 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self._stats = self.Stats()

    def show(self) -> str:
        self._stats.show_call += 1
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def grow(self, amount: float = 1.0) -> None:
        self.height += amount
        self._stats.grow_call += 1

    def age_one_day(self, amount: int = 0) -> None:
        for _ in range(amount):
            self.age += 1
        self._stats.age_call += 1

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365


    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self.grow_call = 0
            self.age_call = 0
            self.show_call = 0
            self.shade_call = 0

        def display_stats(self) -> str:
            return (f"Stats: {self.grow_call} grow, {self.age_call}"
                    f" age, {self.show_call} show")


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
            return (f"{base}\nColor: {self.color}\n{self.name}"
                    f" is blooming beautifully!")
        else:
            return (f"{base}\nColor: {self.color}\n{self.name}"
                    f" has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = int((self.height + self.age) / 5)

    def show(self) -> str:
        base = super().show()
        return f"{base}\nSeeds: {self.seeds}"


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter:
                 float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        self._stats.shade_call += 1
        return (f"Tree {self.name} now produces a shade of {self.height:.1f}cm"
                f" long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> str:
        base = super().show()
        return f"{base}\nTrunk diameter: {self.trunk_diameter:.1f}cm"


def display_statistics(plant: Plant) -> None:
    stats = plant._stats.display_stats()
    print(f"[statistics for {plant.name}]")
    print(stats)


def display_stats_tree(plant: Plant) -> None:
    print(f"{plant._stats.shade_call} shade")


def main() -> None:
    print("=== Garden statistics ===")

    print("====== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")
    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(rose.show())
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    print(rose.show())
    display_statistics(rose)
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print(oak.show())
    display_statistics(oak)
    display_stats_tree(oak)
    print("[asking the oak to produce shade]")
    print(oak.produce_shade())
    display_statistics(oak)
    display_stats_tree(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age_one_day(20)
    sunflower.bloom()
    print(sunflower.show())
    display_statistics(sunflower)
    print("")

    print("=== Anonymous")
    unknown = Plant.anonymous_plant()
    print(unknown.show())
    display_statistics(unknown)


if __name__ == "__main__":
    main()
