class Plant:

	def __init__(self, name: str, height_cm: float, age_d: int):
		self.name = name
		self.height = height_cm
		self.age = age_d
		self._stats = self.Stats()

	def show(self):
		return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

	def grow(self, amount: float = 0.8):
		self.height += amount

	def age_one_day(self):
		self.age += 1

	@staticmethod
	def check_age(age):
		if age > 365 :
			return True
		return False

	@classmethod
	def anonymous_plant(cls):
		return cls("Unknown plant", 0.0, 0)

	class Stats:
		def __init__(self):
			self.grow_call = 0
			self.age_call = 0
			self.show_call = 0

		def display_stats(self):
			return f"Stats: {self.grow_call} grow, {self.age_call} age, {self.show_call} show"




class Flower(Plant):
	def __init__(self, name: str, height_cm: float, age_d: int, color: str):
		super().__init__(name, height_cm, age_d)
		self.color = color
		self.bloomed = False

	def bloom(self):
		self.bloomed = True

	def show(self):
		base = super().show()
		if self.bloomed:
			return(f"{base}\nColor: {self.color}\n{self.name} is blooming beautifully!")
		else:
			return(f"{base}\nColor: {self.color}\n{self.name} has not bloomed yet")

class Seed(Flower):
	pass


class Tree(Plant):
	def __init__(self, name: str, height_cm: float, age_d: int, trunk_diameter: float):
		super().__init__(name, height_cm, age_d)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self):
		return f"Tree {self.name} now produces a shade of {self.height:.1f}m long and {self.trunk_diameter:.1f}cm wide"

	def show(self):
		base = super().show()
		return f"{base}\nTrunk diameter: {self.trunk_diameter:.1f}cm"


class Vegetable(Plant):
	def __init__(self, name: str, height_cm: float, age_d: int, harvest_season: str):
		super().__init__(name, height_cm, age_d)
		self.harvest_season = harvest_season
		self.nutritional_value = 0

	def grow(self, amount: float = 2.1):
		super().grow(amount)
		self.nutritional_value += 1

	def show(self):
		base = super().show()
		return f"{base}\nHarvest season: {self.harvest_season}\nNutritional value: {self.nutritional_value}"


