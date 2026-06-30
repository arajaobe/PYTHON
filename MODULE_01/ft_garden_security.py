#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:03:35 by arajaobe            #+#    #+#            #
#   Updated: 2026/06/02 16:27:31 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height, silent = True)
        self.set_age(age, silent = True)


    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float, silent: bool = False) -> None:
        if new_height < 0:
            if not silent:
                print(f"{self.name}: Error, height can't be negative")
                print("Height update rejected")
        else:
            self._height = new_height
            if not silent:
                print(f"Height updated: {self.get_height():.0f}cm")

    def set_age(self, new_age: int, silent: bool = False) -> None:
        if new_age < 0:
            if not silent:
                print(f"{self.name}: Error, age can't be negative")
                print("Age update rejected")
        else:
            self._age = new_age
            if not silent:
                print(f"Age updated: {self.get_age()} days")

    def show(self) -> str:
        return (f"{self.name}: {self.get_height():.1f}cm, "
                f"{self.get_age()} days old")


def update_plants(plants: Plant, height_value: float,
                  age_value: int) -> None:
    plants.set_height(height_value)
    plants.set_age(age_value)
    print("")


def display_created_plants(plants: Plant) -> None:
    print("=== Garden Security System ===")
    print(f"Plant created: {plants.show()}")
    print("")
    update_plants(plants, 25, 30)
    update_plants(plants, -2, -9)
    print(f"Current state: {plants.show()}")


def main() -> None:
    plants = Plant('Rose', 15, 10)
    display_created_plants(plants)


if __name__ == "__main__":
    main()
