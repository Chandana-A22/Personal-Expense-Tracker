
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Add a new expense
def add_expense():
    print("\n--- ADD EXPENSE ---")

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date! Please use YYYY-MM-DD.")
        return

    category = input("Enter category (Food/Travel/Shopping/Bills/Other): ")

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero!")
            return
    except ValueError:
        print("Invalid amount!")
        return

    description = input("Enter description: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writerow(["Date", "Category", "Amount", "Description"])

        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n--- ALL EXPENSES ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            found = True
            print(
                f"Date: {row['Date']} | "
                f"Category: {row['Category']} | "
                f"Amount: Rs.{row['Amount']} | "
                f"Description: {row['Description']}"
            )

        if not found:
            print("No expenses recorded!")


# Filter expenses by category
def filter_expenses():
    print("\n--- FILTER EXPENSES ---")

    category = input("Enter category to search: ").strip().lower()

    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].strip().lower() == category:
                print(row)
                found = True

    if not found:
        print("No expenses found in this category!")


# Show category-wise total
def category_summary():
    print("\n--- CATEGORY SUMMARY ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    totals = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in totals:
                totals[category] += amount
            else:
                totals[category] = amount

    if not totals:
        print("No expenses recorded!")
        return

    for category, total in totals.items():
        print(f"{category}: Rs.{total:.2f}")


# Main menu
def main():
    while True:
        print("\n================================")
        print("   PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please enter 1 to 5.")


if __name__ == "__main__":
    main()
