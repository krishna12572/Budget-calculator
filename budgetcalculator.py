import datetime 

# Ask the user for the date to use as filename
date_input = input("Enter today's date (YYYY-MM-DD): ")

# Set the filename based on the entered date
filename = f"{date_input}.txt"

total = 0  # Initial balance is 0

while True:
    print("\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Reset Data\n5. Quit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        income = float(input("Enter your total income amount: "))
        total += income
        print("The total income is:", total)

        # Save to file
        with open(filename, "a") as file:
            file.write("The total income is: " + str(total) + "\n")

    elif choice == 2:
        category = input("Enter expense category (food, rent, transport): ").lower()
        amount = float(input(f"Enter amount for {category}: "))
        total -= amount
        print("The total balance is now:", total)

        # Save to file
        with open(filename, "a") as file:
            file.write(f"Expense ({category}): -{amount}\n")

    elif choice == 3:
        print("The total balance is now:", total)

        # Save to file
        with open(filename, "a") as file:
            file.write(f"Summary checked. Current balance: {total}\n")

    elif choice == 4:
        total = 0
        print("Data has been reset. The total balance is now 0.")

        # Save to file
        with open(filename, "a") as file:
            file.write("Data reset. Balance is now 0.\n")

    elif choice == 5:
        print("Thank you for using this app!")
        with open(filename, "a") as file:
            file.write("Session ended.\n")
        break

    else:
        print("Invalid option, please try again with the options provided.")
