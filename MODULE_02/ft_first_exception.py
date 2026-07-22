def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        result = input_temperature(temp_str)
        print(f"Temperature is now {result}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)

def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature("25")
    print("")
    test_temperature("abc")
    print("")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    main()

