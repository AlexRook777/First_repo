pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool/quantity
    print(f'Each mailing will have {chunk} items.')
except IndexError:
    print("Error: Index out of range. The index must be between 0 and 2.")
except ValueError:
    print("Error: Invalid input for index. Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Index cannot be 0 for this division.")
except Exception as e: # Catch any other unexpected error
    print(f"An unexpected error occurred: {e}")