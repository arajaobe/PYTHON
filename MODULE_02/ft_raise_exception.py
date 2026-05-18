def input_temperature(temp_str: str) -> int:
	temp_int = int(temp_str)
	if temp_int < 0:
		raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
	elif temp_int > 40:
		raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
	else:
		return temp_int

def test_temperature(temp_str: str):
	print(f"Input data is '{temp_str}'")
	try:
		result = input_temperature(temp_str)
		print(f"Temperature is now {result}°C")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}")

def main():
	print("=== Garden Temperature Checker ===\n")
	test_temperature("25")
	print("\n")
	test_temperature("abc")
	print("\n")
	test_temperature("100")
	print("\n")
	test_temperature("-50")
	print("\n")
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
	main()
