
import random

def gen_event():
    name_list = ["bob", "dylan", "alice", "charlie"]
    action_list = ["run", "eat", "grab", "move", "sleep", "jump", "climb", "release", "sing", "play"]
    name = random.choice(name_list)
    action = random.choice(action_list)
    yield(name, action)

def consume_event(value: list[tuple[str, str]]):
    result = random.choice(value)
    value.remove(result)
    yield result

def main():
    print("=== Game Data Stream Processor ===")
    i = 0
    while i < 1000:
        result = gen_event()
        name, action = next(result)
        print(f"Event {i}: Player {name} did action {action}")
        i += 1

    list_of_tpl = []
    i = 0
    while i < 10:
        result = gen_event()
        list_of_tpl.append(next(result))
        i += 1

    print("Built list of 10 events:", list_of_tpl)

    length = len(list_of_tpl)
    for _ in range(length):
          print("Got event from list:", next(consume_event(list_of_tpl)))
          print("Remains in list:", list_of_tpl)


if __name__ == "__main__":
	main()
