import codewars_test as test

def find_outlier(integers):
    count_odd = 0
    count_eve = 0
    outlier = 0

    if integers[0] % 2 == 0:
        count_eve += 1
    else:
        count_odd += 1
 
    if integers[1] % 2 == 0:
        count_eve += 1
    else:
        count_odd += 1

    if integers[2] % 2 == 0:
        count_eve += 1
    else:
        count_odd += 1

    if count_eve >= 2:
        for n in integers:
            if n % 2 != 0:
                outlier = n
    elif count_odd >= 2:
        for n in integers:
            if n % 2 == 0:
                outlier = n

    return outlier

#    odds = [x for x in integers if x%2!=0]
#    evens= [x for x in integers if x%2==0]
#    return odds[0] if len(odds)<len(evens) else evens[0]

test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)