import sys

class NegativeError(Exception):
	def __init__(self, message="Error"):
		self.message = message

def input_list(temp_str: str) -> int:
	temp_int = int(temp_str)
	if (temp_int < 0):
		raise NegativeError("Negative value")
	else:
		return temp_int


def list_to_int(value: list[str]) -> int | list[int]:
	temp = value[1:]
	length = len(temp)
	if length < 1:
		return 0
	count = 0
	int_list = []
	for arg in temp:
		try:
			int_list.append(input_list(arg))
		except ValueError:
			count += 1
			print(f"Invalid parameter: '{arg}'")
		except NegativeError as e:
			count += 1
			print(f"{e}: {arg}")
	if count != length:
		return (int_list)
	else:
		return 0


def display_scores(value: list[int]) -> None:
	length = len(value)
	max_val = max(value)
	min_val = min(value)
	sum_val = sum(value)
	print("Total players:", length)
	print("Total score:", sum_val)
	print(f"Average score: {(sum_val / length):.1f}")
	print("High score:", max_val)
	print("Low score:", min_val)
	print("Score range:", max_val - min_val)


def main():
	print("=== Player Score Analytics ===")
	args = sys.argv
	int_lst = list_to_int(args)
	if int_lst == 0:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
	else :
		print("Scores processed:",int_lst)
		display_scores(int_lst)



if __name__ == "__main__":
	main()

