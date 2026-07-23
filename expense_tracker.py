total = 0

while True:
    expense = input("Enter expense (or type 'quit' to exit): ")

    if expense.lower() == "quit":
        break

    try:
        expense = int(expense)
        total += expense
        print("Current Total:", total)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Final Total:", total)