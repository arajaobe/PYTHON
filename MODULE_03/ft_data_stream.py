#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: arajaobe <arajaobe@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/26 12:42:31 by arajaobe            #+#    #+#            #
#   Updated: 2026/07/26 13:05:00 by arajaobe           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    name_list = ["bob", "dylan", "alice", "charlie"]
    action_list = ["run", "eat", "grab", "move", "sleep", "jump",
                   "climb", "release", "sing", "swim", "use"]
    while True:
        yield (random.choice(name_list), random.choice(action_list))


def consume_event(
    value: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(value) > 0:
        result = random.choice(value)
        value.remove(result)
        yield result


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()
    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    list_of_tpl: list[tuple[str, str]] = []
    for _ in range(10):
        list_of_tpl = list_of_tpl + [next(generator)]

    print("Built list of 10 events:", list_of_tpl)

    for event in consume_event(list_of_tpl):
        print("Got event from list:", event)
        print("Remains in list:", list_of_tpl)


if __name__ == "__main__":
    main()
