#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/26 12:41:18 by arajaobe            #+#    #+#            #
#   Updated: 2026/07/26 13:01:25 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def list_to_float(value: list[str]) -> tuple[float, float, float] | None:
    length = len(value)
    if length != 3:
        print("Invalid syntax")
        return None
    float_list: list[float] = []
    for arg in value:
        try:
            float_list = float_list + [float(arg.strip())]
        except ValueError as e:
            print(f"Error on parameter '{arg.strip()}': {e}")
            return None
    return (float_list[0], float_list[1], float_list[2])


def get_player_pos() -> tuple[float, float, float]:
    while True:
        value = input("Enter new coordinates as floats in format 'x,y,z': ")
        lst = value.split(',')
        float_tpl = list_to_float(lst)
        if float_tpl is not None:
            return (float_tpl)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    first_float_tpl = get_player_pos()
    print("Got a first tuple:", first_float_tpl)
    x1, y1, z1 = first_float_tpl

    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_center = math.sqrt(x1**2 + y1**2 + z1**2)
    print("Distance to center:", round(distance_center, 4))

    print("\nGet a second set of coordinates")
    sec_float_tpl = get_player_pos()
    x2, y2, z2 = sec_float_tpl

    distance_two = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print("Distance between the 2 sets of coordinates:",
          round(distance_two, 4))


if __name__ == "__main__":
    main()
