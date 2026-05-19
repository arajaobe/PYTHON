
class GardenError(Exception):
	def __init__(self, message="General garden error"):
		self.message = message

class PlantError(GardenError):
	def __init__(self, message="Unknown plant error"):
		self.message = message

class WaterError(GardenError):
	def __init__(self, message="Watering problem"):
		self.message = message

def test_plant_error():
	raise PlantError("The tomato plant is wilting!")

def test_water_error():
	raise WaterError("Not enough water in the tank!")

def test_custom_errors():
	print("=== Custom Garden Errors Demo ===")
	print("\n")

	print("Testing PlantError...")
	try:
		test_plant_error()
	except PlantError as e:
		print("Caught PlantError:", e)
	print("\n")

	print("Testing WaterError...")
	try:
		test_water_error()
	except WaterError as e:
		print("caught WaterError:", e)
	print("\n")

	print("Testing catching all garden errors...")
	try:
		test_plant_error()
	except PlantError as e:
		print("Caught PlantError:", e)
	try:
		test_water_error()
	except WaterError as e:
		print("caught WaterError:", e)
	print("\n")

	print("All custom error types work correctly!")

def main():
	test_custom_errors()

if __name__ == "__main__":
	main()
