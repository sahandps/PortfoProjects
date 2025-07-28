def get_valid_input(start, end):
    while True:
        try:
            user_input = int(input("Enter a number"))
            if start <= user_input <= end:
                return user_input
            else:
                print("Invalid input please enter a valid number")
                continue
        except ValueError:
            print("Invalid input. Please enter a number")
            continue    