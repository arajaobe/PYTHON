class Plant:

	def __init__(self, name: str, height_cm: float, age_d: int):
		self.name = name
		self.height = height_cm
		self.age = age_d

	def show(self):
		return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

class Flower(Plant):
	def __init__(self, name: str, height_cm: float, age_d: int, color: str):
		super().__init__(name, height_cm, age_d)
		self.color = color

	def bloom(self, called):
		if called:
			print(f"{self.name} is blooming beautifully!")
		else:
			print(f"{self.name} has not bloomed yet")

def flower_state(plants, is_bloom):
	print("===Flower")
	print(plants.show())
	print(f"Color: {plants.color}")
	plants.bloom(is_bloom)

def display_plants(flower_plant):
	print("=== Garden Plant Types ===")
	is_bloom = 1
	flower_state(flower_plant, is_bloom)



def main():
	plants = Flower("Rose", 30, 25, "Red")
	display_plants(plants)




if __name__ == "__main__":
	main()
