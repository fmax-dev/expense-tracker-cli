import argparse

from expense_tracker import (
    load_expenses_file,
    save_expenses,
    timestamp,
    add_expense,
    list_expenses,
    update_expense,
    delete_expense,
)

def main():
    print("\n====== EXPENSES TRACKER ======\n")

    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="A simple Expenses Tracker CLI"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--description", type=str, help="Expense description")
    add_parser.add_argument("--amount", type=int, help="Expense amount")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", type=int, help="Expense ID")
    update_parser.add_argument("--description", type=str, help="New expense description")
    update_parser.add_argument("--amount", type=int, help="New expense amount")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", type=int, help="Expense ID")

    # List command
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Parse the command-line inputs
    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expenses()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()