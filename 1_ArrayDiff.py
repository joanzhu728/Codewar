def array_diff(a, b):
    #your code here
    l1 = len(a)
    l2 = len(b)
    index1 = 0
    
    while index1 < l1:
        index2 = 0
        while index2 < l2:
            if a[index1] == b[index2]:
                a.pop(index1)
                if a != []:
                    index1 -= 1
                    l1 = len(a)
            index2 += 1
        index1 += 1

    return a
#    return [x for x in a if x not in b]

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
        test.assert_equals(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")