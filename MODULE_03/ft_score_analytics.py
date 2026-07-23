import sys


def list_to_int(value: list[str]) -> list[int]:
    temp = value[1:]
    int_list = []
    for arg in temp:
        try:
            int_list = int_list + [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return int_list


def display_scores(value: list[int]) -> None:
    length = len(value)
    max_val = max(value)
    min_val = min(value)
    sum_val = sum(value)
    print("Scores processed:", value)
    print("Total players:", length)
    print("Total score:", sum_val)
    try:
        print(f"Average score: {(sum_val / length):.1f}")
    except OverflowError:
        print("Average score: too large to compute")
    print("High score:", max_val)
    print("Low score:", min_val)
    print("Score range:", max_val - min_val)


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv
    int_lst = list_to_int(args)
    if not int_lst:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        display_scores(int_lst)


if __name__ == "__main__":
    main()

