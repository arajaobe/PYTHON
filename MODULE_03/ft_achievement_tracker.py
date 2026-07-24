#!/usr/bin/env python3
import random

class Player:
    def __init__(self, name: str, achievements: set[str] | None = None) -> None:
        self.name = name
        self.achievements = achievements if achievements is not None else set()


def gen_player_achievements(achievements_list: list[str]) -> set[str]:

    length = len(achievements_list)
    number = random.randint(3, length)
    set_achievements = set(random.sample(achievements_list, k=number))
    return (set_achievements)

def main() -> None:
    print("=== Achievement Tracker System ===\n")

    achievements_list = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor','Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer', 'Hidden Path Finder']
    set_achievements = set(achievements_list)

    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Dylan")
    player4 = Player("Charlie")

    player1.achievements = gen_player_achievements(achievements_list)
    player2.achievements = gen_player_achievements(achievements_list)
    player3.achievements = gen_player_achievements(achievements_list)
    player4.achievements = gen_player_achievements(achievements_list)

    print(f"Player {player1.name}: {player1.achievements}\n")
    print(f"Player {player2.name}: {player2.achievements}\n")
    print(f"Player {player3.name}: {player3.achievements}\n")
    print(f"Player {player4.name}: {player4.achievements}\n")

    unique_achievements = set.union(player1.achievements, player2.achievements, player3.achievements, player4.achievements)
    common_achievements = set.intersection(player1.achievements, player2.achievements, player3.achievements, player4.achievements)

    print("All distinct achievements:", unique_achievements)
    print("\nCommon achievements:", common_achievements)
    print("")

    print(f"Only {player1.name} has:", set.difference(player1.achievements, set.union(player2.achievements, player3.achievements, player4.achievements)))
    print(f"Only {player2.name} has:", set.difference(player2.achievements, set.union(player1.achievements, player3.achievements, player4.achievements)))
    print(f"Only {player3.name} has:", set.difference(player3.achievements, set.union(player1.achievements, player2.achievements, player4.achievements)))
    print(f"Only {player4.name} has:", set.difference(player4.achievements, set.union(player2.achievements, player3.achievements, player1.achievements)))

    print("")

    print(f"{player1.name} is missing:", set.difference(set_achievements, player1.achievements))
    print(f"{player2.name} is missing:", set.difference(set_achievements, player2.achievements))
    print(f"{player3.name} is missing:", set.difference(set_achievements, player3.achievements))
    print(f"{player4.name} is missing:", set.difference(set_achievements, player4.achievements))

if __name__ == "__main__":
    main()
