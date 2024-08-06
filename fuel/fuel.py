def calculate_percentage(fraction):
    try:
        # Split the fraction into X and Y
        x, y = map(int, fraction.split('/'))

        # Check if Y is 0 or X is greater than Y
        if y == 0 or x > y:
            return None

        # Calculate the fuel percentage
        percentage = (x / y) * 100

        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return str(round(percentage)) + '%'

    except ValueError:
        return None


def main():
    while True:
        # Prompt the user for a fraction
        fraction = input("Enter the fraction (X/Y) representing the fuel level: ")

        # Call calculate_percentage to get the fuel percentage
        percentage = calculate_percentage(fraction)

        if percentage is not None:
            # Print the fuel percentage and break the loop
            print(percentage)
            break
        else:
            # Invalid fraction, prompt the user again
            print("Invalid fraction. Please try again.")


if __name__ == "__main__":
    main()
