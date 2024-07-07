expenses = []
expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '21.55', 'category': 'groceries'}
expenses.append(expense2)

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    for counter, expense in enumerate(expenses):
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
    print("\n")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("How much was this expense?")
            while True:
                try:
                    amountToAdd = float(input("> "))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

            print("What category was this expense?")
            category = input("> ")
            addExpense(amountToAdd, category)
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        else:
            print("Invalid input. Please try again.")
