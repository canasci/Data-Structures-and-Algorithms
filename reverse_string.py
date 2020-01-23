# method 1
def reverse_str(string: str) -> str:        # 0(n)
    if (type(string) != str) or (len(string) < 2):
        return string
    else:
        str_list = []
        for i in range(len(string)):    # O(n)
            # split_str = string.strip()
            str_list.append(string[-i - 1])
        rev_str = ''.join(str_list)     # O(n)
        return rev_str


print(reverse_str('sample string'))

# method 2
str1 = 'sample'
reversed_string = ''.join(reversed(str1))    # O(n)
print(reversed_string)

# method 3
x = lambda str_1: ''.join(reversed(str_1))
print(x('sample'))

