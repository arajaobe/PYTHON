def garden_operations(operation_number: str) -> int:
	operation_result = int(operation_number)
	raise ZeroDivisionError("division by zero")
	raise FileNotFoundError("division by zero")
	

def test_temperature(temp_str: str):
	print(f"Input data is '{temp_str}'")
	try:
		result = garden_operations(temp_str)
		print(f"Temperature is now {result}°C")
	except ValueError as e:
		print(f"Caught input_temperature error: {e}")
