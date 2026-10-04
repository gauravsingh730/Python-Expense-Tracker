#Expense Tracker
      #Mini Project
expensesList = [] # list of expenses in form of dictionary 
print("Welcome to Expense Tracker!")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    # Get user choice directly (assumes the user will type a valid integer)
    choice = int(input("Please Enter Your Choice: "))

    # 1. Add Expense
    if choice == 1:
        date = input("Enter date (e.g., YYYY-MM-DD): ")
        category = input("Enter category (e.g., Food, Rent, Travel): ")
        
        # Get amount directly (assumes the user will type a valid number)
        amount = float(input("Enter amount: "))
            
        description = input("Enter a short description: ")
        
        # Create a dictionary for the new expense
        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        
        # Add the dictionary to the main list
        expensesList.append(expense)
        print("Expense added successfully!")

    # 2. View All Expenses
    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            for index, exp in enumerate(expensesList, 1):
                print(f"{index}. Date: {exp['date']} | Category: {exp['category'].title()} | Amount: {exp['amount']:.2f} | Desc: {exp['description']}")
            print("--------------------")

    # 3. View Total Expenses
    elif choice == 3:
        if len(expensesList) == 0:
            print("Total Expenses: 0.00")
        else:
            # Calculate the sum of all 'amount' values in the list of dictionaries
            total = sum(exp['amount'] for exp in expensesList)
            print(f" Total Expenses: {total:.2f}")

    # 4. Exit
    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break

    # Handle numbers outside 1-4
    else:
        print("Invalid choice. Please select a valid option (1-4).")