import csv
from datetime import datetime

# Define the CSV file where data will be stored
FILE_NAME = 'budget.csv'

# Initialize the CSV file with headers if it doesn't exist
def initialize_csv():
    try:
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Description', 'Category', 'Amount', 'Type'])
    except FileExistsError:
        pass

# Function to add a budget entry
def add_entry():
    date = datetime.now().strftime('%Y-%m-%d')
    description = input("Enter the description: ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    entry_type = input("Enter the type (income/expense): ").lower()

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount, entry_type])
    print("Entry added successfully!")

# Function to view all budget entries
def view_entries():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No entries found. Please add entries first.")

# Function to summarize budget entries by category
def summarize_entries():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            entries = list(reader)[1:]
            summary = {}
            for entry in entries:
                category = entry[2]
                amount = float(entry[3])
                entry_type = entry[4]
                if category not in summary:
                    summary[category] = {'income': 0, 'expense': 0}
                if entry_type == 'income':
                    summary[category]['income'] += amount
                else:
                    summary[category]['expense'] += amount

            print("Budget Summary by Category:")
            for category, totals in summary.items():
                print(f"{category} - Income: ${totals['income']:.2f}, Expense: ${totals['expense']:.2f}")
    except FileNotFoundError:
        print("No entries found. Please add entries first.")

if __name__ == '__main__':
    initialize_csv()  # Initialize the CSV file with headers
    
    # Main loop to interact with the user
    while True:
        print("\n1. Add Entry")
        print("2. View Entries")
        print("3. Summarize Entries")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            summarize_entries()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

##Explanation:
##Initialization: Creates a CSV file with headers if it doesn’t exist.

##Adding Entries: Appends a new budget entry to the CSV file.

##Viewing Entries: Reads and prints all budget entries from the CSV file.

##Summarizing Entries: Summarizes budget entries by category and type (income or expense) and prints totals.

##Enhancements:
##User Input: Modify the script to take input from users for adding entries.

##Date Filters: Add functionality to filter entries by date.

##Advanced Analysis: Use libraries like pandas for more complex data analysis and visualization.
