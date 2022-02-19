def count_bits(n):
    count = 0
    bi = str(bin(n))
    bi = bi[2:]
    for x in bi:
        if x == "1":
            count += 1
    return count

    # return bin(n).count("1")

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count_bits(0), 0)
        test.assert_equals(count_bits(4), 1)
        test.assert_equals(count_bits(7), 3)
        test.assert_equals(count_bits(9), 2)
        test.assert_equals(count_bits(10), 2)