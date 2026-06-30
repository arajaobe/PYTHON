#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:03:46 by arajaobe            #+#    #+#            #
#   Updated: 2026/05/28 18:01:56 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 0.8):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_day_one(self) -> None:
        self.age += 1


def simulate_week_growth(plant: Plant) -> None:
    print("=== Garden Plant Growth ===")
    print(plant.show())

    initial_height = plant.height
    for day in range(1, 8):
        plant.age_day_one()
        plant.grow()
        print(f"=== Day {day} ===")
        print(plant.show())

    final_height = plant.height - initial_height
    print(f"Growth this week: {final_height:.1f}cm")


def main() -> None:
    plants = Plant("Rose", 25.0, 30, 0.8)
    simulate_week_growth(plants)


if __name__ == "__main__":
    main()
