
class Plant:

	def __init__(self, name, height_cm, age_d):
		self.name = name
		self.height = height_cm
		self.age = age_d

	def show(self):
		return f"{self.name}: {self.height}cm, {self.age} days old"

def display_plants(item1, item2, item3):
	print("=== Garden Plant Registry ===")
	print(item1.show())
	print(item2.show())
	print(item3.show())

def main():
	plant1 = Plant('Rose', 25, 30)
	plant2 = Plant('Sunflower', 80, 45)
	plant3 = Plant('Cactus', 15, 120)
	display_plants(plant1, plant2, plant3)


if __name__ == "__main__":
	main()
