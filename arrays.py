strings= ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5]
# Variable array is somewhere in memory and the computer knows it.
# When I do array[2], i'm telling the computer, hey go to the array and grab the 3rd item from where the array is stored.

# push
strings.append('e')     # O(1) in Python3, might be O(n) in another language

# pop
strings.pop()       # O(1)
strings.pop()

# unshift       # O(n)
strings.insert(0, 'x')

# splice
strings.insert(2, 'alien')      # O(n)

print(strings)
