
import sys
import typing

def read_file(f: typing.IO[str]) -> str:
    content = f.read()
    print("---\n")
    print(content)
    print("---")
    return content


def transform(content: str) -> str:
    lines = content.splitlines()
    new_content = [line + "#" for line in lines]
    return "\n".join(new_content)


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    f = open(filename, "w")
    f.write(content)
    f.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        sys.stderr.write("[STDERR] Usage: ft_ancient_text.py <file>\n")
        sys.stderr.flush()
        return
    filename = sys.argv[1]
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")
    sys.stdout.flush()
    try:
        f = open(filename, "r")
        content = read_file(f)
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return

    print("\nTransform data:")
    new_content = transform(content)
    print(f"---\n\n{new_content}\n\n---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().rstrip()
    if new_filename:
        try:
            save_file(new_filename, new_content)
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{new_filename}': {e}\n")
            sys.stderr.flush()
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()


