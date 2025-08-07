# Budget Tracker CLI Application

## Overview
This is a console-based Budget Tracker application built in Python. It allows users to manage their income and expenses through a simple Command-Line Interface (CLI). The application uses Object-Oriented Programming (OOP) principles, file handling, and provides a user-friendly interface for tracking financial transactions.

## Features
- **Add Transaction**: Record income or expense with amount, category, and optional notes.
- **List All Transactions**: Display all transactions in a readable format.
- **Filter Transactions**: Filter by type (income/expense) or category.
- **View Summary**: Show total income, total expenses, and net balance.
- **Save and Load Transactions**: Persist data in `transactions.txt` and load on startup.

## Requirements
- Python 3.6 or higher
- No external libraries are required.

## How to Run
1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd budget-tracker
   ```
3. Run the application:
   ```bash
   python budget_tracker.py
   ```
4. Follow the on-screen menu to interact with the application.

## File Structure
- `budget_tracker.py`: Main application code.
- `transactions.txt`: Auto-generated file to store transaction data (pipe-separated format).
- `README.md`: This file.

## Usage
- On startup, the application loads existing transactions from `transactions.txt` (if it exists).
- Use the menu to:
  - **Add a transaction**: Enter type (income/expense), amount, category, and optional notes.
  - **List transactions**: View all recorded transactions.
  - **Filter transactions**: Filter by type or category.
  - **View summary**: See total income, expenses, and net balance.
  - **Exit**: Save transactions and close the application.
- Transactions are automatically saved to `transactions.txt` after each addition.

## Notes
- The application validates user input (e.g., numeric amounts, valid transaction types).
- Data is stored in a pipe-separated format in `transactions.txt` for simplicity.
- The application handles file I/O errors gracefully and provides feedback for invalid inputs.

## Example `transactions.txt` Format
```
income|1000.0|Salary|Monthly paycheck|2025-08-07 11:10:00
expense|50.0|Food|Groceries|2025-08-07 11:10:00
```
