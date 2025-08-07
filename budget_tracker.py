# budget_tracker.py
# A console-based budget tracker application using OOP principles
# Features: Add transactions, list transactions, filter transactions, view summary, save/load to file

import os
from datetime import datetime

class Transaction:
    """Represents an individual transaction (income or expense)."""
    def __init__(self, trans_type, amount, category, notes=""):
        self.trans_type = trans_type.lower()  # 'income' or 'expense'
        self.amount = float(amount)
        self.category = category
        self.notes = notes
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        """String representation of the transaction."""
        return f"{self.date} | {self.trans_type.capitalize():7} | ${self.amount:8.2f} | {self.category:15} | {self.notes}"

    def to_file_format(self):
        """Format transaction for file storage (pipe-separated)."""
        return f"{self.trans_type}|{self.amount}|{self.category}|{self.notes}|{self.date}\n"

class BudgetTracker:
    """Manages a collection of transactions and provides CLI operations."""
    def __init__(self, filename="transactions.txt"):
        self.transactions = []
        self.filename = filename
        self.load_transactions()

    def add_transaction(self, trans_type, amount, category, notes=""):
        """Add a new transaction to the collection."""
        try:
            # Validate transaction type
            if trans_type.lower() not in ["income", "expense"]:
                raise ValueError("Transaction type must be 'income' or 'expense'.")
            # Validate amount
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            # Validate category
            if not category.strip():
                raise ValueError("Category cannot be empty.")
            transaction = Transaction(trans_type, amount, category, notes)
            self.transactions.append(transaction)
            self.save_transactions()
            print("Transaction added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def list_transactions(self):
        """Display all transactions in a formatted manner."""
        if not self.transactions:
            print("No transactions found.")
            return
        print("\nAll Transactions:")
        print("-" * 70)
        print("Date                | Type    | Amount    | Category        | Notes")
        print("-" * 70)
        for trans in self.transactions:
            print(trans)
        print("-" * 70)

    def filter_transactions(self, filter_type=None, category=None):
        """Filter transactions by type or category."""
        filtered = self.transactions
        if filter_type:
            filter_type = filter_type.lower()
            if filter_type not in ["income", "expense"]:
                print("Error: Filter type must be 'income' or 'expense'.")
                return
            filtered = [t for t in filtered if t.trans_type == filter_type]
        if category:
            filtered = [t for t in filtered if t.category.lower() == category.lower()]
        if not filtered:
            print("No transactions match the criteria.")
            return
        print(f"\nFiltered Transactions (Type: {filter_type or 'All'}, Category: {category or 'All'}):")
        print("-" * 70)
        print("Date                | Type    | Amount    | Category        | Notes")
        print("-" * 70)
        for trans in filtered:
            print(trans)
        print("-" * 70)

    def view_summary(self):
        """Display total income, expenses, and net balance."""
        total_income = sum(t.amount for t in self.transactions if t.trans_type == "income")
        total_expense = sum(t.amount for t in self.transactions if t.trans_type == "expense")
        net_balance = total_income - total_expense
        print("\nFinancial Summary:")
        print(f"Total Income:  ${total_income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Net Balance:    ${net_balance:.2f}")

    def save_transactions(self):
        """Save all transactions to the file."""
        try:
            with open(self.filename, 'w') as file:
                for trans in self.transactions:
                    file.write(trans.to_file_format())
        except IOError as e:
            print(f"Error saving transactions: {e}")

    def load_transactions(self):
        """Load transactions from the file."""
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    trans_type, amount, category, notes, date = line.strip().split("|")
                    trans = Transaction(trans_type, float(amount), category, notes)
                    trans.date = date  # Preserve original date
                    self.transactions.append(trans)
        except (IOError, ValueError) as e:
            print(f"Error loading transactions: {e}")

def main():
    """Main function to run the CLI application."""
    tracker = BudgetTracker()

    while True:
        print("\n=== Budget Tracker Menu ===")
        print("1. Add Transaction")
        print("2. List All Transactions")
        print("3. Filter Transactions")
        print("4. View Summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            trans_type = input("Enter transaction type (income/expense): ").lower()
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                notes = input("Enter notes (optional): ")
                tracker.add_transaction(trans_type, amount, category, notes)
            except ValueError:
                print("Error: Invalid amount. Please enter a number.")

        elif choice == "2":
            tracker.list_transactions()

        elif choice == "3":
            filter_type = input("Enter type to filter (income/expense, or press Enter for all): ")
            category = input("Enter category to filter (or press Enter for all): ")
            tracker.filter_transactions(filter_type or None, category or None)

        elif choice == "4":
            tracker.view_summary()

        elif choice == "5":
            print("Exiting Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()