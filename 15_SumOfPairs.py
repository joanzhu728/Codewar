def sum_pairs(ints, s):
    max = len(ints)
    i = 0
    dic = {}

    while i < max:
        if dic.get(ints[i]) == None:
            dic[(s - ints[i])] = i
            i += 1
        else:
            return [(s - ints[i]), ints[i]]
    return None

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

    # Solution 2
    # max = len(ints)
    # w = 1

    # while w < max:
    #     i = 0
    #     while i + w < max:
    #         if ints[i] + ints[i + w] == s:
    #             return [ints[i], ints[i + w]]
    #         else:
    #             i += 1
    #     w += 1
    # return None

    # Solution 1
    # max = len(ints)
    # i = 0
    # w = max
    # l = []

    # while i < max:
    #     j = i + 1
    #     while j < i + w and j < max:
    #         if ints[i] + ints[j] == s:
    #             w = j - i
    #             l = [ints[i], ints[j]]
    #             break
    #         else:
    #             j += 1
    #     i += 1
    
    # if l == []: return None
    # else: return l


import codewars_test as test
test.describe("Testing For Sum of Pairs")
test.expect(sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
test.expect(sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
test.expect(sum_pairs(l3, -7) == None, "No Match: %s should return None for sum = -7" % l3)
test.expect(sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
