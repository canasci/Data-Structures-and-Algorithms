class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        elif self.length == 1:
            self.first.next = newNode
            self.last.next = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self.last.data

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            holdingPointer = self.first
            self.last = None
            self.length -= 1
            return holdingPointer.data
        else:
            holdingPointer = self.first
            print(holdingPointer)
            self.first = self.first.next
            self.length -= 1
            return holdingPointer.data

    def print_queue(self):
        currentNode = self.first
        for i in range(myQueue.length):
            print(currentNode.data)
            currentNode = currentNode.next


if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue('Can')
    myQueue.enqueue('Burak')

    myQueue.print_queue()
    print()
    print(myQueue.peek())
    print()
    print(myQueue.dequeue())
    myQueue.print_queue()
