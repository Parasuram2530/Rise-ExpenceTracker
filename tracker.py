import datetime

expenses = []

def show_menu():
    print("\n===== Expense Tracker CLI =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")

def add_expense():
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        category = input("Enter Category (e.g., 'Food', 'Travel'): ")
        amount = int(input("Enter the Amount that Spent: ₹"))

        expense = {
            "date": date_str,
            "category": category,
            "amount": amount
        }
        expenses.append(expense)
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid input! Please try again.")

def show_expenses():
    if not expenses:
        print("⚠️ No Expenses Recorded Yet!")
        return

    print("\n📋 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. Date: {exp['date']} | Category: {exp['category']} | Amount: ₹{exp['amount']}")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Select from menu (1-3): "))
        except ValueError:
            print("❌ Please enter a number (1-3)!")
            continue

        if choice == 1:
            add_expense()
        elif choice == 2:
            show_expenses()
        elif choice == 3:
            print("👋 Exiting... Byeee!")
            break
        else:
            print("❌ Please Enter a Value ranging between 1-3! Try Again...")

if __name__ == "__main__":
    main()








