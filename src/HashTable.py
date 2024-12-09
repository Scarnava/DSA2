class HashTable:
    def __init__(self, size=40):  # Adjust size based on expected number of packages
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Hash function to map keys to table indices."""
        return key % len(self.table)

    def insert(self, package_id, package_data):
        """Insert package data into the hash table."""
        index = self._hash(package_id)
        for entry in self.table[index]:
            if entry[0] == package_id:
                entry[1] = package_data  # Update if package ID already exists
                return
        self.table[index].append([package_id, package_data])  # Add new entry

    def lookup(self, package_id):
        """Retrieve package data by package ID."""
        index = self._hash(package_id)
        for entry in self.table[index]:
            if entry[0] == package_id:
                return entry[1]  # Return package data if found
        return None  # Return None if package ID is not found

    def display(self):
        """Display the contents of the hash table (for debugging)."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
