def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your invoice amount is {amount:.2f} is due: {due_date}")


display_invoice("Alice", 100.50, "2023-10-01")
