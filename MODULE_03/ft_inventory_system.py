#!/usr/bin/env python3
import sys

def parse_items(value: str)->dict[str, int]:
	liste = value.split()
	list_of_list = []
	list_of_key = []
	list_of_value = []
	for arg in liste:
		lst1 = arg.split(':')
		if len(lst1) != 2:
			print(f"invalid parameter: '{lst1[0]}'")
		else:
			second_list = []
			if lst1[0] in list_of_key:
				print(f"Redundant item '{lst1[0]}' - discarding")
			else:
				second_list.append(lst1[0])
			list_of_key.append(lst1[0])
			try:
				second_list.append(int(lst1[1]))
			except ValueError as e:
				print(f"Quantity error for '{lst1[0]}':", e)
			if len(second_list) == 2:
				list_of_list.append(second_list)
				list_of_value.append(int(lst1[1]))
	d = dict(list_of_list)
	return d

def max_int(value: list[int])->int:
	max = value[0]

	for arg in value[1:]:
		if arg > max:
			max = arg
	return max


def min_int(value: list[int])->int:
	min = value[0]

	for arg in value[1:]:
		if arg < min:
			min = arg
	return min

def find_key(value_str: list[str], value_int: list[int], number = int)->str:
	res = -1

	for arg in value_int:
		res += 1
		if arg == number:
			break
	return value_str[res]


def main():
	print("=== Inventory System Analysis ===")
	value_dict = {}
	value_str = ' '.join(sys.argv[1:])
	if len(value_str) < 1:
		print("Inventory is empty:", value_dict)
	else :
		value_dict = parse_items(value_str)
		if not value_dict:
			print("Inventory is empty:", value_dict)
			return
		list_of_keys = []
		list_of_values = []
		for arg in value_dict:
			list_of_keys.append(arg)

		for arg in value_dict.values():
			list_of_values.append(arg)

		total = sum(list_of_values)
		print("Got inventory:",value_dict)
		print("Item list:", list_of_keys)
		print(f"Total quantity of the {len(list_of_keys)} items:", total)

		i  = 0
		for arg in list_of_keys:
			print(f"Item {arg} represents {round((list_of_values[i] / total) * 100, 1)}%")
			i += 1
		max_val = max_int(list_of_values)
		min_val = min_int(list_of_values)
		print(f"Item most abundant: {find_key(list_of_keys, list_of_values, max_val)} with quantity {max_val}")
		print(f"Item least abundant: {find_key(list_of_keys, list_of_values, min_val)} with quantity {min_val}")

		value_dict.update({"magic item" : 1})
		print("Updated inventory:", value_dict)

if __name__ == "__main__":
	main()

