def calculate_current():
    voltage = float(input("Enter voltage: "))
    resistance = float(input("Enter resistance: "))

    if resistance <= 0:
        print("Error!! Resistance must be greater than zero")
    else:
        current = voltage / resistance
        print(f"Current is: {current} A")


def calculate_voltage():
    current = float(input("Enter current: "))
    resistance = float(input("Enter resistance: "))

    if resistance < 0:
        print("Error!! Resistance cannot be negative")
    else:
        voltage = current * resistance
        print(f"Voltage is: {voltage} V")


def calculate_resistance():
    voltage = float(input("Enter voltage: "))
    current = float(input("Enter current: "))

    if current == 0:
        print("Error!! Current cannot be zero")
    else:
        resistance = voltage / current
        print(f"Resistance is: {resistance} Ohms")


def calculate_power():
    voltage = float(input("Enter voltage: "))
    current = float(input("Enter current: "))

    power = current * voltage
    print(f"Power is: {power} W")


def calculate_series_resistance():
    resistors = []

    number = int(input("How many resistors? "))

    if number <= 0:
        print("Error!! Number of resistors must be greater than zero")
        return

    for i in range(number):
        resistance = float(input(f"Enter resistance R{i + 1}: "))

        if resistance < 0:
            print("Error!! Resistance cannot be negative")
            return

        resistors.append(resistance)

    total_resistance = sum(resistors)
    print(f"Total resistance is: {total_resistance} Ohms")


def calculate_parallel_resistance():
    resistors = []

    number = int(input("How many resistors? "))

    if number <= 0:
        print("Error!! Number of resistors must be greater than zero")
        return

    for i in range(number):
        resistance = float(input(f"Enter resistance R{i + 1}: "))

        if resistance <= 0:
            print("Error!! Resistance must be greater than zero")
            return

        resistors.append(resistance)

    total = sum(1 / r for r in resistors)
    total_resistance = 1 / total

    print(f"Total resistance is: {total_resistance} Ohms")


def calculate_voltage_divider():
    input_voltage = float(input("Enter input voltage: "))
    r1 = float(input("Enter R1: "))
    r2 = float(input("Enter R2: "))

    if r1 < 0 or r2 < 0:
        print("Error!! Resistance cannot be negative")
    elif r1 + r2 == 0:
        print("Error!! The total resistance cannot be zero")
    else:
        output_voltage = input_voltage * (r2 / (r1 + r2))
        print(f"Output voltage is: {output_voltage} V")


def calculate_current_divider():
    total_current = float(input("Enter total current: "))
    r1 = float(input("Enter R1: "))
    r2 = float(input("Enter R2: "))

    if r1 < 0 or r2 < 0:
        print("Error!! Resistance cannot be negative")
    elif r1 + r2 == 0:
        print("Error!! The total resistance cannot be zero")
    else:
        current_r1 = total_current * (r2 / (r1 + r2))
        current_r2 = total_current * (r1 / (r1 + r2))

        print(f"Current through R1 is: {current_r1} A")
        print(f"Current through R2 is: {current_r2} A")


print("       ELECTRICAL CALCULATOR    ")

option = """
1. Calculate current
2. Calculate voltage
3. Calculate resistance
4. Calculate power
5. Calculate series resistance
6. Calculate parallel resistance
7. Calculate voltage divider
8. Calculate current divider
9. Exit
"""

print(option)

while True:

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            calculate_current()

        elif choice == 2:
            calculate_voltage()

        elif choice == 3:
            calculate_resistance()

        elif choice == 4:
            calculate_power()

        elif choice == 5:
            calculate_series_resistance()

        elif choice == 6:
            calculate_parallel_resistance()

        elif choice == 7:
            calculate_voltage_divider()

        elif choice == 8:
            calculate_current_divider()

        elif choice == 9:
            print("Exiting the program")
            break

        else:
            print("Invalid choice")
            print("Try again")

    except ValueError:
        print("Invalid input!! Please enter a number")
