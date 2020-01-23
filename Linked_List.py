# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # append method for the linked list
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = self.head
        elif self.head and self.length > 1:
            self.tail.next = new_node
            self.tail = self.tail.next
        elif self.head and self.length == 1:
            self.head.next = new_node
            self.tail = self.head.next
        self.length += 1

    # prepend method for the linked list
    def prepend(self, data):
        new_node = Node(data, next=self.head)
        self.head = new_node
        self.length += 1

    # insert method for the linked list
    def insert(self, index, data):
        if index == self.length:
            self.append(data)
        else:
            if index == 0:
                self.prepend(data)
            else:
                new_node = Node(data)
                leader = self.traverse_to_index(index - 1)
                holding_pointer = leader.next
                leader.next = new_node
                new_node.next = holding_pointer
                self.length += 1

    def traverse_to_index(self, index):
        if self.length > 0:
            counter = 0
            current_node = self.head
            while counter != index:
                current_node = current_node.next
                counter += 1
            return current_node

    def search(self, value):
        if self.length > 0:
            current_node = self.head
            while current_node.next is not None:
                if current_node.data == value:
                    return True
                else:
                    current_node = current_node.next
            return False

    # print method for the linked list
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == '__main__':
    LL = LinkedList()
    LL.append(3)
    LL.append(4)
    LL.append(5)
    LL.append(11)
    LL.insert(0, 10)
    LL.insert(2, 88)
    LL.prepend(13)
    LL.print_linked_list()
    print(LL.search(11))
