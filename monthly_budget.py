def budget_tracker():
    print("--- Monthly Budget Tracker ---")
    
    # Get initial budget
    try:
        balance = float(input("Enter your total monthly budget: "))
    except ValueError:
        print("Please enter a valid number for the budget.")
        return

    print("\nEnter your expenses one by one. Type 'done' when you are finished.")
    
    while True:
        user_input = input("Enter expense amount (or 'done'): ").strip().lower()
        
        if user_input == 'done':
            break
        
        try:
            expense = float(user_input)
            balance -= expense
            print(f"Current Balance: {balance:.2f} LKR")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    # Final Summary
    print("\n" + "="*30)
    print(f"Final Remaining Balance: {balance:.2f} LKR")
    
    # Low funds warning
    if balance < 500:
        print("Warning: Low Funds")
    print("="*30)

if __name__ == "__main__":
    budget_tracker()