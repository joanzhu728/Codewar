import codewars_test as test

def persistence(n):
    times = 0
    if len(str(n)) == 1:
        return times
    else:
        while len(str(n)) > 1:
            multiple = 1
            for x in str(n):
                multiple *= int(x)
            times += 1
            n = multiple
        return times

# import operator
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i

test.it("Basic tests")
test.assert_equals(persistence(39), 3)
test.assert_equals(persistence(4), 0)
test.assert_equals(persistence(25), 2)
test.assert_equals(persistence(999), 4)