from src.HashTable import HashTable

if __name__ == "__main__":
    table = HashTable()
    table.insert(1, {"address": "123 Main St", "deadline": "10:30 AM"})
    print(table.lookup(1))
