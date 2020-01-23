class MyArray(object):
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):   # O(1)
        return self.data[index]

    def push(self, value):   # O(1)
        self.data[self.length] = value
        self.length += 1
        return self.data

    def pop(self):   # O(1)
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete_at_index(self, index):   # O(n) due to shifting
        item = self.data[index]
        self.shift_items_del(index)
        return item

    def insert_at_index(self, index, item):   # O(n) due to shifting
        self.shift_items_add(index)
        self.data[index] = item
        return item

    def shift_items_del(self, index):   # O(n)
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1

    def shift_items_add(self, index):   # O(n)
        for i in range(index + 1, self.length + 1)[::-1]:
            self.data[i] = self.data[i - 1]
        self.length += 1


if __name__ == '__main__':
    myArray = MyArray()
    myArray.push('hi')
    myArray.push('you')
    myArray.push('!')
    myArray.pop()
    myArray.delete_at_index(0)
    myArray.push('are')
    myArray.push('nice')
    myArray.shift_items_del(0)
    myArray.push('how')
    myArray.push('you')
    print(myArray.data)
    myArray.insert_at_index(0, 'can')
    print(myArray.data)
