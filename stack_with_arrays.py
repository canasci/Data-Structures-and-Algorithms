class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()


if __name__ == '__main__':
    myStack = Stack()
    myStack.push('can')
    myStack.push('burak')
    myStack.push('fuat')
    print(myStack.array)
    myStack.pop()
    print()
    myStack.pop()
    myStack.pop()
    print(myStack.array)
