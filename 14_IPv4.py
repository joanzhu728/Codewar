def int32_to_ip(int32):
    b = bin(int32)[2:].zfill(32)
    i = 0
    l_bin = []
    l_int = []

    while  i < 32:
        l_bin.append(b[i:i+8])
        i += 8

    for x in l_bin:
        if x == '00000000':
            l_int.append('0')
        else:
            l_int.append(int(x, 2))

    l_str = [str(x) for x in l_int]
    return '.'.join(l_str)


import codewars_test as test
test.assert_equals(int32_to_ip(2154959208), "128.114.17.104") 
test.assert_equals(int32_to_ip(0), "0.0.0.0")
test.assert_equals(int32_to_ip(2149583361), "128.32.10.1")
test.assert_equals(int32_to_ip(285304087), "17.1.101.23") 
test.assert_equals(int32_to_ip(2048792), "0.31.67.24") 