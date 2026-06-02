
def secure_archive(filename: str, action: str="r", content: str="" ) -> tuple[bool, str]:
	if action == "r":
		try:
			with open(filename, "r") as f:
				content_file = f.read()
			print("Using 'secure_archive' to read from a regular file:")
			return(True, content_file)
		except FileNotFoundError as e:
			print("Using 'secure_archive' to read from a nonexistent file:")
			return(False, f"{e}")
		except PermissionError as e:
			print("Using 'secure_archive' to read from an inaccessible file:")
			return(False, f"{e}")
	elif action == "w":
		try:
			with open(filename, "w") as f:
				f.write(content)
			print("Using 'secure_archive' to write previous content to a new file:")
			return (True, "Content successfully written to file")
		except Exception as e:
			print("Using 'secure_archive' to write previous content to a new file:")
			return(False, f"{e}")
	else:
		return None

def main():
	print("=== Cyber Archives Security ===\n")

	result = secure_archive("not/existing/file")
	print(result)
	print("\n")
	result = secure_archive("ask.passwd")
	print(result)
	print("\n")
	result = secure_archive("ancient_fragment.txt")
	print(result)
	print("\n")
	result = secure_archive("result.txt", "w", "bonjour")
	print(result)


if __name__ == "__main__":
	main()


