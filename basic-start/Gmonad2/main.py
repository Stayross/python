while True:
    user_input = input("Please enter a number from 1 to 10: ")

    if user_input.isdigit():
        number = int(user_input)
        if 1 <= number <= 10:
            for _ in range(number):
                print("GMONAD")
            break
        else:
            print("Number must be between 1 and 10.")
    else:
        print("Enter a numeric value.")