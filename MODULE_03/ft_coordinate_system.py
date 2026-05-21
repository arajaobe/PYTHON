import math

def list_to_float(value: list[str]) -> int | tuple[float]:
	length = len(value)
	if length != 3:
		return 0
	lst_tmp = []
	tmp = ' '.join(value)
	lst_tmp = tmp.split()
	length = len(lst_tmp)
	if length != 3:
		return 0
	count = 0
	float_list = []
	for arg in lst_tmp:
		try:
			float_list.append(round(float(arg), 1))
		except ValueError:
			count = 1
			print (f"Invalid parameter: '{arg}'")
	res_tuple = tuple(float_list)
	if count:
		return count
	return (res_tuple)


def get_player_pos() -> tuple[float]:
	i = 0
	while i == 0:
		lst = []
		value = input("Enter new coordinates as floats in format 'x,y,z': ")
		lst = value.split(',')
		float_tpl = list_to_float(lst)
		if float_tpl == 0:
			print("Invalid syntax")
		elif float_tpl == 1:
			pass
		else:
			i = 1
	return (float_tpl)

def main():
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

	distance_two = math.sqrt((x2-x1)**2 +(y2-y1)**2 + (z2-z1)**2)
	print("Distance between the 2 sets of coordinates:", round(distance_two, 4))

if __name__ == "__main__":
	main()
