#!/usr/bin/env python3
import random

def is_capitalize(value: str)->int:
	if value[0].isupper():
		return 1
	return 0

def capitalizer(value: list[str])->list[str]:
	res = [arg.capitalize() for arg in value]
	return res

def only_capitalize(value: list[str])->list[str]:
	res = [arg for arg in value if is_capitalize(arg)]
	return res

def main():
	print("=== Game Data Alchemist ===\n")

	players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
	print("Initial list of players:", players)

	list_key = capitalizer(players)
	list_only_capitalize = only_capitalize(players)

	print("New list with all names capitalized:", list_key)
	print("New list of capitalized names only:", list_only_capitalize)
	print("\n")

	score_dict = {name : random.randint(1, 1000) for name in list_key}
	list_score = list(score_dict.values())
	average = round(sum(list_score) / len(list_key), 2)
	high_score_dict = {key : value for key, value in score_dict.items() if value > average }

	print("Score dict:", score_dict)
	print("Score average:", average)
	print("High scores:", high_score_dict)

if __name__ == "__main__":
	main()
