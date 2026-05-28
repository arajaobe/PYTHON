#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/28 13:03:35 by arajaobe            #+#    #+#            #
#   Updated: 2026/05/28 13:03:41 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height_cm: float, age_d: int):
        self.name = name
        self._height = height_cm
        self._age = age_d
        if self._height < 0 or self._age < 0:
            print("Error, value can't be negative")
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print("Height updated successfully !")
            print(f"New height: {self.get_height():.1f} days")


    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print("Age updated successfully !")
            print(f"New age: {self.get_age()} days")


    def show(self):
        return f"{self.name}: {self.get_height():.1f}cm, {self.get_age()} days old"


def update_plants(plants, height_value=0, age_value=0):
    plants.set_height(height_value)
    plants.set_age(age_value)
    print("\n")


def display_created_plants(plants):
    print("=== Garden Security System ===")
    print(f"Plant created: {plants.show()}")
    print("\n")
    update_plants(plants, 56, 23)
    update_plants(plants, 69, 233)
    print(f"Current state: {plants.show()}")

def main():
    plants = Plant('Rose', 25, 89)
    if plants.get_height() > 0 and plants.get_age() > 0:
        display_created_plants(plants)


if __name__ == "__main__":
    main()
