import codewars_test as test

def create_phone_number(n):
    i = 0
    n1 = ""
    n2 = ""
    n3 = ""
    
    for n in n: 
        if i < 3:
            n1 += str(n)
        elif i < 6:
            n2 += str(n)
        elif i < 10:
            n3 += str(n)
        i += 1

    
    return "(" + n1 + ")" + " " + n2 + "-" + n3
        
#    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#    n = ''.join(map(str,n))
#    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

test.describe("Basic tests")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")