
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

print(new_content)

f.close()


