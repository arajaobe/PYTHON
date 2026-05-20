
import sys

def main():
	arguments = sys.argv
	length = len(arguments)
	print("=== Command Quest ===")
	print("Program name:", arguments[0])
	if length < 2:
		print("No arguments provided!")
	else:
		temp = arguments[1:]
		print(f"Arguments received: {length - 1}")
		i = 1
		for arg in temp:
			print(f"Argument {i}: {arg}")
			i += 1
	print(f"Total arguments: {length}")


if __name__ == "__main__":
	main()
