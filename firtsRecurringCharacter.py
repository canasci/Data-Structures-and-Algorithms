# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2
#
# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1
#
# Given an array = [2,3,4,5]:
# It should return undefined


def first_recurring_character0(array):
    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[i] == array[j]:
                return input[i]
    return None

# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# return 5 because the pairs are before 2,2


def first_recurring_character1(array):
    keys_dict = {}
    for i in range(len(array)):
        if array[i] in keys_dict.keys():
            return array[i]
        else:
            keys_dict[array[i]] = i
    return None


def first_recurring_character2(lst: list):
    element_set = set(lst)
    if len(lst) == len(element_set):
        return None
    index_lst = []
    for item in element_set:
        n = 0
        for index, element in enumerate(lst):
            if element == item:
                n += 1
                if n == 2:
                    index_lst.append(index)
    return lst[min(index_lst)]


def first_recurring_character3(lst: list):
    recurr_array = set(lst)
    if len(lst) == len(recurr_array):
        return None
    for item in recurr_array:
        n = 0
        for element in lst:
            if element == item:
                n += 1
                if n == 2:
                    return element


print(first_recurring_character1([2, 5, 5, 2, 3, 5, 1, 2, 4]))
first_recurring_character1([1, 5, 5, 1, 3, 4, 6])
