def swap(l, i, j):
    l[j], l[i] = l[i], l[j]

def permutations(string):
    out = set()
    out = recurse(string, 0, out)
    return out

def recurse(string, j, out):
    max = len(string)
    l = list(string)
    s = ''

    if max == 1:
        return l
 
    if j == max - 1:
        out.add(s.join(l))

    for i in range(j, max):
        swap(l, j, i)
        recurse(s.join(l), j + 1, out)
        swap(l, j, i)
    
    return out




import codewars_test as test
test.assert_equals(sorted(permutations('a')), ['a'])
test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
test.assert_equals(sorted(permutations('abc')), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])