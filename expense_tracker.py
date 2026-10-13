import decimal
import os
import json
import argparse
from datetime import datetime

# A JSON file as DB to store users expenses.
EXPENSES_FILE = "expenses.json"

# LOAD or CREATE the file
def load_expenses_file():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)

    return {"last_id": 0, "expenses": []}

# Save expenses data to file
def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Formatted date as YYYY-MM-DD
def timestamp():
    today = datetime.today().date()
    formatted_date = today.strftime("%Y-%m-%d")
    return formatted_date

# Add Command
def add_expense(description, amount):
    expense_data = load_expenses_file()

    # Generating expense ID
    expense_data['last_id'] += 1
    expense_id = expense_data['last_id']

    # Append the tasks to the file
    expense_data["expenses"].append(
        {
            "id": expense_id,
            "description": description,
            "amount": amount,
            "date": timestamp()
        }
    )

    save_expenses(expense_data)
    print(f"Expense added successfully (ID: {expense_id})")


# List command
def list_expenses():
    expense_data = load_expenses_file()

    if not expense_data["expenses"]:
        print("No expenses found, please add your first expense")
        return

    # Print the header row with defined column widths
    print(f"{"ID":<8}{"Date":<15}{"Description":<20}{"Amount"}")
    #print("-" * 50) # Visual separator line

    for item in expense_data["expenses"]:
        # Extract the fields safely using their keys
        id_val = item.get("id", "")
        date_val = item.get("date", "")
        description_val = item.get("description", "")
        amount_val = item.get("amount", 0)

        # Print the formatted row
        print(f"{id_val:<8}{date_val:15}{description_val:<20}${amount_val:.2f}")