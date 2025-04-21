import datetime 

# user need to enter the date
date_input = input("Enter today's date (YYYY-MM-DD): ")

# Set the filename based on the entered date
filename = f"{date_input}.txt"

total = 0  # Initial balance is 0

while True:
    print("\n1. Enter Income\n2. Enter Expense\n3. Summary table\n4. Reset Data\n5. Quit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        income = float(input("Enter your total income : "))
        total += income
        print("The total income is:", total)

        # Save to file
        with open(filename, "a") as file:
            file.write("The total income is: " + str(total) + "\n")

    elif choice == 2:
        used = input("Enter how the income was used: ").lower()
        amount = float(input(f"Enter amount for {used}: "))
        total -= amount
        print("The total balance is now:", total)

        # Save to file
        with open(filename, "a") as file:
            file.write(f"Expense ({used}): -{amount}\n")

    elif choice == 3:
        print("The total balance is now:", total)

        # Save to file
        with open(filename, "a") as file:
            file.write(f"Summary checked. Current balance: {total}\n")

    elif choice == 4:
        total = 0
        print("Data is reset. The  balance is  0.")

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
