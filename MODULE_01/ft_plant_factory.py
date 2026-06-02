#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:02:58 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/02 15:30:20 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height_cm: float, age_d: int,
                 grow_rate: float = 0.8):
        self.name = name
        self.height = height_cm
        self.age = age_d
        self.growth_rate = grow_rate

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_day_one(self) -> None:
        self.age += 1


def display_created_plants(plants: list[Plant]) -> None:
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.show()}")


def main() -> None:
    plants = [
        Plant('Rose', 25.0, 30),
        Plant('Sunflower', 80.0, 45),
        Plant('Cactus', 5.0, 90),
        Plant('Oak', 200.0, 365),
        Plant('Fern', 15.0, 120)
    ]

    display_created_plants(plants)


if __name__ == "__main__":
    main()
