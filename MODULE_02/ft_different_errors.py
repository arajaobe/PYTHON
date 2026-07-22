def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "test" + 6
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    value = [0, 1, 2, 3, 4]
    print("=== Garden Error Types Demo ===")
    for i in value:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print("Caught ValueError:", e)
        except ZeroDivisionError as e:
            print("Caught ZeroDivisionError:", e)
        except FileNotFoundError as e:
            print("Caught FileNotFoundError:", e)
        except TypeError as e:
            print("Caught TypeError:", e)

    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()

if __name__ == "__main__":
    main()
