def duplicate_count(text):
    i = 0
    text = text.upper()
    for x in text:
        if text.count(x) > 1:
            i += 1
            text = text.replace(x,"")
    return i

#   return len([c for c in set(text.lower()) if text.lower().count(c)>1])

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)