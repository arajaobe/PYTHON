
import sys
import typing

def read_file(f: typing.IO) -> None:
	print("---\n")
	print(f.read())
	print("---")

def main() -> None:
	if len(sys.argv) != 2:
		print("Usage: ft_ancient_text.py <file>")
		return
	filename = sys.argv[1]
	print("=== Cyber Archives Recovery ===")
	print(f"Accessing file '{filename}'")
	try:
		f = open(filename, "r")
		read_file(f)
		f.close()
		print(f"File '{filename}' closed.")
	except Exception as e:
		print(f"Error opening file '{filename}':", e)

if __name__ == "__main__":
	main()
