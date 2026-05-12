
class Plant:

	def __init__(self, name, height_cm, age_d):
		self.name = name
		self.height = height_cm
		self.age = age_d

	def show(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

def display_plants(plants):
	print("=== Garden Plant Registry ===")
	for plant in plants:
		print(plant.show())

def main():
	plants = [
			Plant('Rose', 25, 30),
			Plant('Sunflower', 80, 45),
			Plant('Cactus', 15, 120)
	]

	display_plants(plants)


if __name__ == "__main__":
	main()
