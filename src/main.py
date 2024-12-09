from src.HashTable import HashTable

"""
Main module for testing the HashTable implementation.
"""

def main():
    """
    Tests the insertion and lookup functionality of the HashTable class.
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

    # Insert package data
    package_table.insert(1, package_1)
    package_table.insert(2, package_2)

    # Retrieve and display package data
    print("Package 1 Data:", package_table.lookup(1))
    print("Package 2 Data:", package_table.lookup(2))

    # Test lookup for a non-existent package
    print("Package 3 Data:", package_table.lookup(3))  # Expect None

    # Display hash table contents
    package_table.display()

if __name__ == "__main__":
    main()
