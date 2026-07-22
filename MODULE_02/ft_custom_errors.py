
class GardenError(Exception):
    def __init__(self, message: str ="Unknown plant error") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str ="Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str ="Unknown plant error") -> None:
        super().__init__(message)

def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")

def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")

def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("")

    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print("Caught PlantError:", e)
    print("")

    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print("caught WaterError:", e)
    print("")

    print("Testing catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print("Caught GardenError:", e)
    try:
        test_water_error()
    except GardenError as e:
        print("Caught GardenError:", e)
    print("")

    print("All custom error types work correctly!")

def main() -> None:
    test_custom_errors()

if __name__ == "__main__":
    main()
