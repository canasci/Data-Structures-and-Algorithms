class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1
        return self

    def pop(self):
        if not self.top:
            return None
        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
            self.length -= 1
            return self.top

    def print_stack(self):
        if self.length > 1:
            currentNode = self.top
            for i in range(self.length):
                print(currentNode.data)
                currentNode = currentNode.next
                if currentNode is None:
                    break
        elif self.length == 1:
            print(self.bottom)


if __name__ == '__main__':
    myStack = Stack()
    myStack.push('can')
    myStack.push('burak')
    myStack.push('fuat')
    myStack.print_stack()
    myStack.pop()
    myStack.pop()
    myStack.pop()
    myStack.print_stack()
    print()
    myStack.push(10)
    myStack.print_stack()
    print(myStack.length)
