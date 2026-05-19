
class GardenError(Exception):
	def __init__(self, message="General garden error"):
		self.message = message

class PlantError(GardenError):
	def __init__(self, message="Unknown plant error"):
		self.message = message

class WaterError(GardenError):
	def __init__(self, message="Watering problem"):
		self.message = message


def water_plant(plant_name: str):
	if plant_name == plant_name.capitalize():
		print (f"Watering {plant_name}: [OK]")
	else:
		raise WaterError(f"Invalid plant name to water: '{plant_name}'")

def test_watering_systerm(plants):
	print("Opening watering system")
	try:
		for plant in plants:
			water_plant(plant)
	except WaterError as e:
		print("Caught PlantError:", e)
		print(".. ending tests and returning to main")
	finally:
		print("Closing watering system")


def main():
	print("=== Garden Watering System ===")
	print("\n")

	print("Testing valid plants...")
	test_watering_systerm(["Tomato", "Lettuce", "Carrots"])
	print("\n")

	print("Testing invalid plants...")
	test_watering_systerm(["Tomato", "lettuce", "Carrots"])
	print("\n")

	print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
	main()
