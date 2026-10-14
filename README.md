# Expense Tracker

Simple terminal-based expense tracker for managing personal finances. Add, update, delete, and view expenses, and get a quick summary of your spending to stay on budget.

## Table of Contents
- [Feature Overview](#feature-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Project Source](#project-source)

## Feature Overview

- Add an expense with a description and amount — auto-assigned an incrementing ID and today's date
- List all expenses in a clean, column-aligned table
- Update an expense's description and/or amount by ID
- Delete an expense by ID
- View a summary of total expenses across all entries
- View a summary of expenses for a specific month
- Stores data locally in a JSON file (`expenses.json`) — no external dependencies, uses Python's standard library only

## Installation

To install this program, use the commands below:

```bash
git clone https://github.com/fmax-dev/expense-tracker-cli.git
cd expense-tracker-cli
```

No packages to install. Requires Python 3.12+.

## Usage

```bash
python main.py <command> [options]
```

**Example:**

```bash
python main.py add --description "Groceries" --amount 85
# Expense added successfully (ID: 1)

python main.py add --description "Coffee" --amount 6
# Expense added successfully (ID: 2)

python main.py list
# ID      Date           Description         Amount
# 1       2026-10-14     Groceries           $85.00
# 2       2026-10-14     Coffee              $6.00

python main.py update --id 2 --amount 8
# Expense with ID 2 updated successfully.

python main.py summary
# Total expenses: $93.00

python main.py delete --id 1
# Expense with ID 1 deleted successfully.

python main.py summary
# Total expenses: $8.00

python main.py summary --month 10
# Total expenses for month 10: $8.00
```

## Commands

| Command | Options | Description |
|---|---|---|
| `add` | `--description`, `--amount` | Add a new expense |
| `list` | — | List all expenses |
| `update` | `--id`, `--description`, `--amount` | Update an existing expense's description and/or amount |
| `delete` | `--id` | Delete an expense by ID |
| `summary` | `--month` (optional) | Show total expenses, or total for a specific month |

## Project Source

This project is from [roadmap.sh](https://roadmap.sh). [Click here](https://roadmap.sh/projects/expense-tracker) to check it out.
