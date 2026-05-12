
class Plant:

	def __init__(self, name, height_cm, age_d, growth_rate=0.8):
		self.name = name
		self.height = height_cm
		self.age = age_d
		self.growth_rate = growth_rate

	def show(self):
		return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

	def grow(self):
		self.height += self.growth_rate

	def age_day_one(self):
		self.age += 1

def simulate_week_growth(plant):
	print("=== Garden Plant Growth ===")
	print(plant.show())

	initial_height = plant.height
	for day in range(1, 8):
		plant.age_day_one()
		plant.grow()
		print(f"== Day {day} ===")
		print(plant.show())

	final_height = plant.height - initial_height
	print(f"Growth this week: {final_height:.1f} cm")


def main():
	plants = Plant("Rose", 25.0, 30, 0.8)
	simulate_week_growth(plants)


if __name__ == "__main__":
	main()
