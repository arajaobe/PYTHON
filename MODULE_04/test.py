
import sys
import typing

f = open("ancient_fragment.txt", "r+")

content = f.read()
pos = content.find("\n")
char = "#"

lines = content.splitlines()
content_list = [line + char for line in lines if line]
new_content = "\n".join(content_list)

def save_file(filename: str, content: str) -> None:
	print(f"Saving data to '{filename}'")
	f = open(filename, "w")
	f.write(content)
	f.close()
	print(f"Data saved in file '{filename}'.")



#new_content_str = "".join(new_content)

#print(new_content)

def secure_archive(filename: str, action: str="r", content: str="" ) -> tuple[bool, str]:
	if action == "r":
		try:
			with open(filename, "r") as f:
				content_file = f.read()
			res = True
		except FileNotFoundError as e:
			error = e
			error_message = "Using 'secure_archive' to read from a nonexistent file:"
			res = False
		except PermissionError as e:
			error = e
			error_message = "Using 'secure_archive' to read from an inaccessible file:"
			res = False
		if res:
			print("Using 'secure_archive' to read from a regular file:")
			return (res, content_file)
		else:
			print(error_message)
			return(res, error)
	elif action == "w":
		try:
			with open(filename, "w") as f:
				f.write(content)
			res = True
		except Exception as e:
			error = e
			res = False
		if res:
			return (res, "'Content successfully written to file'")
		else:
			return (res, error)

#print(secure_archive("ancient_fragmnt.txt", "r"))




print(secure_archive("ancient_ragment.txt", "w"))









f.close()


