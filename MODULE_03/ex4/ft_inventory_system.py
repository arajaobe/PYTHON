#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/26 12:42:10 by arajaobe            #+#    #+#            #
#   Updated: 2026/07/26 16:38:09 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys


def parse_items(args: list[str]) -> dict[str, int]:
    d: dict[str, int] = {}
    for arg in args:
        lst = arg.split(':')
        if len(lst) != 2 or not lst[0] or not lst[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if lst[0] in d.keys():
            print(f"Redundant item '{lst[0]}' - discarding")
            continue
        res = lst[0].strip()
        if not res:
            print(f"Error - invalid parameter '{arg[0]}'")
            continue
        try:
            d.update({lst[0].strip(): int(lst[1])})
        except ValueError as e:
            print(f"Quantity error for '{lst[0].strip()}':", e)
    return d


def max_int(value: list[int]) -> int:
    maximum = value[0]
    for arg in value[1:]:
        if arg > maximum:
            maximum = arg
    return maximum


def min_int(value: list[int]) -> int:
    minimum = value[0]
    for arg in value[1:]:
        if arg < minimum:
            minimum = arg
    return minimum


def find_key(keys: list[str], values: list[int], number: int) -> str:
    for i in range(len(keys)):
        if values[i] == number:
            return keys[i]
    return ""


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("Inventory is empty: {}")
        return
    value_dict = parse_items(sys.argv[1:])
    if not value_dict:
        print("Inventory is empty: {}")
        return
    list_of_keys = list(value_dict.keys())
    list_of_values = list(value_dict.values())
    total = sum(list_of_values)
    print("Got inventory:", value_dict)
    print("Item list:", list_of_keys)
    print(f"Total quantity of the {len(list_of_keys)} items:", total)
    for i in range(len(list_of_keys)):
        print(f"Item {list_of_keys[i]} represents "
              f"{round((list_of_values[i] / total) * 100, 1)}%")
    max_val = max_int(list_of_values)
    min_val = min_int(list_of_values)
    print(f"Item most abundant: {find_key(list_of_keys,
                                          list_of_values, max_val)}"
          f" with quantity {max_val}")
    print(f"Item least abundant: {find_key(list_of_keys,
                                           list_of_values, min_val)}"
          f" with quantity {min_val}")
    value_dict.update({"magic_item": 1})
    print("Updated inventory:", value_dict)


if __name__ == "__main__":
    main()
