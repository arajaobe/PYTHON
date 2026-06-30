#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:03:14 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/02 14:38:28 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def display_plants(plants: list[Plant]) -> None:
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant.show())


def main() -> None:
    plants = [
            Plant('Rose', 25, 30),
            Plant('Sunflower', 80, 45),
            Plant('Cactus', 15, 120)
    ]

    display_plants(plants)


if __name__ == "__main__":
    main()
