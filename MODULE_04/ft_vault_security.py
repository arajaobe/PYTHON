
def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    if action == "r":
        try:
            with open(filename, "r") as f:
                return (True, f.read())
        except Exception as e:
            return (False, str(e))
    elif action == "w":
        try:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    return (False, "Invalid action")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", result[1]))


if __name__ == "__main__":
    main()