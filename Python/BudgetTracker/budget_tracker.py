#Tested with initial budget set at 1000 and 3 expenses, Travel, Groceries, and Clothes with a remaining budget of 394

import json #needed to import the json module to handle saving and loading data

def add_expense(expenses, description, amount): # Function to add a new expense to the list of expenses
    expenses.append({"description": description, "amount": amount}) # Add a new expense
    print(f"Added expense: {description}, Amount: {amount}")

def get_total_expenses(expenses): # Function to calculate the total of all expenses
    sum = 0 #initialize the sum to 0
    for expense in expenses: #going through each expense
        sum += expense["amount"] #Adding the amount of each expense to the sum
    return sum

def get_balance(budget, expenses): # Function to calculate the remaining balance
    return budget - get_total_expenses(expenses) #subtract total expenses from budget

def show_budget_details(budget, expenses): # Function to display budget details
    print(f"Total Budget: {budget}") #Display the total budget
    print("Expenses:") #Show each expense
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}") #List each expense description and amount
    print(f"Total Spent: {get_total_expenses(expenses)}") #Show total expenses
    print(f"Remaining Budget: {get_balance(budget, expenses)}") #Show remaining budget

def load_budget_data(filepath): #Function to load budget data from a file (JSON format)
    try:
        with open(filepath, 'r') as file: #Open the file in read mode
            data = json.load(file) #Load the JSON data from the file
            return data["initial_budget"], data["expenses"] #Return initial budget and expenses
    except(FileNotFoundError, json.JSONDecodeError):
        return 0, [] #if file is not found or there is an error, return default values

def save_budget_details(filepath, initial_budget, expenses): # Function to save the budget details back to the JSON file
    data = {
        "initial_budget": initial_budget, # Save initial budget
        "expenses": expenses # Save list of expenses
    }
    with open(filepath, 'w') as file: # Open the file in write mode
        json.dump(data, file, indent=4) #Save data as JSON with indentation for readability

def main(): # Main Function
    print("Welcome to the Budget App")
    #Load budget data from file IF file exists
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath) #Load budget and expenses
    if initial_budget == 0: #If budget and expenses don't exist ask the user to input initial budget
        initial_budget = float(input("What is your initial budget: "))
    budget = initial_budget #Set the current budget

    while True: #Show choices to user
        print("\nPlease pick an option:")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ") #Get the user's choice

        #Handle each choice based on user input
        if choice == "1":
            description = input("Enter expense description: ") #Get Description of expense
            amount = float(input("Enter expense amount: ")) #Get the amount of the expense
            add_expense(expenses, description, amount) # Add the expense
        elif choice == "2":
            show_budget_details(budget, expenses) # Display the budget details
        elif choice == "3":
            save_budget_details(filepath, initial_budget, expenses) #Save budget and expenses
            print("Exiting Budget App. Goodbye!")
            break # Break loop to exit the program
        else:
            print("Invalid choice. Please try again.") # Handle invalid inputs

if __name__ == "__main__":
    main()