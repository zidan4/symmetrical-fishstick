class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append a node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    # Display the list (forward and backward)
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            last_node = current
            current = current.next
        print("None")

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # Delete a node
    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                # If the node is the head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    if current.next:
                        current.next.prev = current.prev
                    if current.prev:
                        current.prev.next = current.next
                return
            current = current.next

    # Detect Cycle (Floyd’s Cycle Detection Algorithm)
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
