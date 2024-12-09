#Student ID:011758846

from src.HashTable import HashTable

"""
Main module for testing and demonstrating the HashTable functionality.
"""

def main():
    """
    Runs the main program that allows users to look up package details dynamically.
    """
    # Create a hash table
    package_table = HashTable()

    # Test data for packages
    package_1 = {
        "address": "123 Main St",
        "deadline": "10:30 AM",
        "city": "Salt Lake City",
        "zip": "84101",
        "weight": 5,
        "status": "At Hub",
        "delivery_time": None
    }
    package_2 = {
        "address": "456 Elm St",
        "deadline": "12:00 PM",
        "city": "Salt Lake City",
        "zip": "84102",
        "weight": 10,
        "status": "At Hub",
        "delivery_time": None
    }

    # Insert package data into the hash table
    package_table.insert(1, package_1)
    package_table.insert(2, package_2)

    print("Welcome to the WGUPS Package Lookup System!")

    # User input for package lookup
    while True:
        try:
            # Prompt user for a package ID
            user_input = input("Enter a package ID to look up (or 'exit' to quit): ")

            # Exit condition
            if user_input.lower() == 'exit':
                print("Thank you for using the system. Goodbye!")
                break

            # Validate input
            package_id = int(user_input)

            # Lookup package data
            package_data = package_table.lookup(package_id)
            if package_data:
                print(f"\nPackage {package_id} Details:")
                for key, value in package_data.items():
                    print(f"  {key}: {value}")
                print()  # Add a blank line for better readability
            else:
                print(f"Package {package_id} not found.\n")

        except ValueError:
            print("Invalid input. Please enter a valid package ID.\n")

if __name__ == "__main__":
    main()
