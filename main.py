# my practice hash table code
class Node:
    def __init__(self, key, info, value):
        self.key = key
        self.value = value
        self.info = info
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, info, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, info, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, info, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        index = self._hash(key)

        current = self.table[index]
        while current:
            if current.key == key:
                return current.info
            current = current.next

        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)

        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False


# Create a hash table with a capacity of 25
ht = HashTable(25)

# Add new members with info
ht.insert("Roman Kornev", "info of Roman", 1)  # here we add member in index (3)
ht.insert("Pavel Ershov", "info of Pavel", 1)  # here we add member AGAIN in index (3)
ht.insert("Aboba Abobavich", "info of Aboba", 2)
ht.insert("Artem Kotlov", "info of Artem", 3)

# Search by name
print(ht.search("Roman Kornev"))  # we can see current info
print(ht.search("Pavel Ershov"))  # cuz we use method "Separate Chaining" for hash table
print(ht.search("Aboba Abobavich"))  # aboba

# Check the size of table
print(len(ht))
