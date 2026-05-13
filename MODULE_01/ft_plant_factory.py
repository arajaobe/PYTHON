
class Plant:

	def __init__(self, name, height_cm, age_d):
		self.name = name
		self.height = height_cm
		self.age = age_d

	def show(self):
		return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

def display_created_plants(plants):
	print("=== Plant Factory Output ===")
	for plant in plants:
		print(f"Created: {plant.show()}")

def main():
	plants = [
			Plant('Rose', 25.0, 30),
			Plant('Sunflower', 80.0, 45),
			Plant('Cactus', 5.0, 90),
			Plant('Oak', 200.0, 365),
			Plant('Fern', 15.0, 120)
	]

	display_created_plants(plants)


if __name__ == "__main__":
	main()
