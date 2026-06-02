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

    def __init__(self, name: str, height_cm: float, age_d: int):
        self.name = name
        self._height = height_cm
        self._age = age_d
        if self._height < 0 or self._age < 0:
            print("Error, value can't be negative")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self.get_height():.1f} days")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self.get_age()} days")

    def show(self) -> str:
        return (f"{self.name}: {self.get_height():.1f}cm, "
                f"{self.get_age()} days old")


def update_plants(plants: Plant, height_value: float = 0,
                  age_value: int = 0) -> None:
    plants.set_height(height_value)
    plants.set_age(age_value)
    print("\n")


def display_created_plants(plants: Plant) -> None:
    print("=== Garden Security System ===")
    print(f"Plant created: {plants.show()}")
    print("\n")
    update_plants(plants, 56, 23)
    update_plants(plants, -2, -9)
    print(f"Current state: {plants.show()}")


def main() -> None:
    plants = Plant('Rose', 25, 89)
    if plants.get_height() > 0 and plants.get_age() > 0:
        display_created_plants(plants)


if __name__ == "__main__":
    main()
