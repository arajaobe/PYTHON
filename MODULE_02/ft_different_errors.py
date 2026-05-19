def garden_operations(operation_number: int):
	if operation_number == 0:
		return int('abc')
	elif operation_number == 1:
		return 10 / 0
	elif operation_number == 2:
		with open("non/existent/file", "r") as f:
			return f
	elif operation_number == 3:
		return "test" + 6
	else:
		return "Operation completed successfully"


def test_error_types():
	value = [2, 1, 6 , 3, 4]
	print("=== Garden Error Types Demo ===")
	for i in value:
		print(f"Testing operation {i}...")
		try:
			result = garden_operations(i)
			print(result)
		except ValueError as e:
			print("Caught ValueError:", e)
		except ZeroDivisionError as e:
			print("Caught ZeroDivisionError:", e)
		except FileNotFoundError as e:
			print("Caught FileExistsError:", e)
		except TypeError as e:
			print("Caught TypeError:", e)

	print("All error types tested successfully!")


def main():
	test_error_types()

if __name__ == "__main__":
	main()
