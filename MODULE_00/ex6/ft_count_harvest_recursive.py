
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(counter, days):
        if counter > days:
            print("Harvest time!")
            return
        print(f"Day {counter}")
        helper(counter + 1, days)
    helper(1, days)
