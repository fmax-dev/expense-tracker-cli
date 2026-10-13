import argparse

from expense_tracker import (
    load_expenses_file,
    save_expenses,
    timestamp,
    add_expense, list_expenses,
)

def main():
    print("\n====== EXPENSES TRACKER ======")
    load_expenses_file()

    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="A simple Expenses Tracker CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--description", type=str, help="Expense description")
    add_parser.add_argument("--amount", type=int, help="Expense amount")

    # List command
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Parse the command-line inputs
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()