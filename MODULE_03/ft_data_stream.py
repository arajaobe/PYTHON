
import random

def gen_event(action_list: list[str], name_list: list[str], n: int):
	for _ in range(n):
		name = random.choice(name_list)
		action = random.choice(action_list)
		yield(name, action)

def consume_event(value: list[tuple[str, str]], n):
	for _ in range(n):
		yield (value.pop())

def main():
	name_list = ["bob", "dylan", "alice", "charlie"]
	action_list = ["run", "eat", "grab", "move", "sleep", "jump", "climb", "release", "sing", "play"]
	print("=== Game Data Stream Processor ===")
	i = 0
	for n, a in gen_event(action_list, name_list, 1000):
		print(f"Event {i} : Player {n} did action {a}")
		i += 1

	list_of_tpl = []
	for t in gen_event(action_list, name_list, 10):
		list_of_tpl.append(t)

	print("Built list of 10 events:", list_of_tpl)

	n = len(list_of_tpl)
	for t in consume_event(list_of_tpl, n):
		print("Got event from list:", t)
		print("Remains in list:",list_of_tpl)


if __name__ == "__main__":
	main()
