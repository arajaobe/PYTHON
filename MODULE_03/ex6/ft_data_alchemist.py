#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/26 12:40:59 by arajaobe            #+#    #+#            #
#   Updated: 2026/07/26 13:04:42 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def is_capitalize(value: str) -> bool:
    return value[0].isupper()


def capitalizer(value: list[str]) -> list[str]:
    res = [arg.capitalize() for arg in value]
    return res


def only_capitalize(value: list[str]) -> list[str]:
    res = [arg for arg in value if is_capitalize(arg)]
    return res


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print("Initial list of players:", players)

    list_key = capitalizer(players)
    list_only_capitalize = only_capitalize(players)

    print("New list with all names capitalized:", list_key)
    print("New list of capitalized names only:", list_only_capitalize)
    print("")

    score_dict = {name: random.randint(1, 1000) for name in list_key}
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    high_score_dict = {key: value for key, value in score_dict.items()
                       if value > average}

    print("Score dict:", score_dict)
    print(f"Score average is {average}")
    print("High scores:", high_score_dict)


if __name__ == "__main__":
    main()
