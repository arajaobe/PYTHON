
import sys
import typing

def read_file(f: typing.IO) -> str:
	content = f.read()
	print("---\n")
	print(content)
	print("---")
	return content


def transform(content: str) -> str:
	lines = content.splitlines()
	new_content = [line + "#" for line in lines if line]
	return "\n".join(new_content)

def save_file(filename: str, content: str) -> None:
	print(f"Saving data to '{filename}'")
	f = open(filename, "w")
	f.write(content)
	f.close()
	print(f"Data saved in file '{filename}'.")

def main() -> None:
	if len(sys.argv) != 2:
		print("Usage: ft_ancient_text.py <file>")
		return
	content = ""
	filename = sys.argv[1]
	print("=== Cyber Archives Recovery ===")
	print(f"Accessing file '{filename}'")
	try:
		f = open(filename, "r")
		content = read_file(f)
		f.close()
		print(f"File '{filename}' closed.")
	except Exception as e:
		print(f"Error opening file '{filename}':", e)
		return

	print("\nTransform data:")
	new_content = transform(content)
	print(f"---\n\n{new_content}\n\n---")
	new_filename = input("Enter new file name (or empty):")
	if new_filename:
		save_file(new_filename, new_content)
	else:
		print("Not saving data.")


if __name__ == "__main__":
	main()


