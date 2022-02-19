class RomanNumerals:
    dic = {"I":"1", "IV":"4", "V":"5", "X":"10", "L":"50", "C":"100", "D":"500", "M":"1000"}
    print(dic)

    def to_roman(val):
        out = ""
        DicVal = list(RomanNumerals.dic.values())
        DicKey = list(RomanNumerals.dic.keys())
        while val > 0:
            if val >= 1000:
                tho = val // 1000
                out += tho * "M"
                val %= 1000
            elif val >= 800:
                hun1 = val // 100
                hun2 = hun1 * 100
                hun3 = (1000 - hun2) // 100
                out += hun3 * "C" + "M"
                val -= hun2
            elif val >= 500:
                hun1 = val // 100
                hun2 = hun1 * 100
                hun3 = (hun2 - 500) // 100
                out += "D" + hun3 * "C" 
                val -= hun2
            elif val >= 300:
                hun1 = val // 100
                hun2 = hun1 * 100
                hun3 = (500 - hun2) // 100
                out += hun3 * "C" + "D"
                val -= hun2
            elif val >= 100:
                hun1 = val // 100
                out += hun1 * "C" 
                val %= 100
            elif val >= 80:
                ten1 = val // 10
                ten2 = ten1 * 10
                ten3 = (100 - ten2) // 10
                out += ten3 * "X" + "C"
                val -= ten2
            # elif val >= 50:
            # elif val >= 30:
            # elif val >= 10:
            # elif val >= 8:
            # elif val >= 5:
            # elif val >= 3:
            # elif val >= 1:
        return out

    def from_roman(roman_num):
        return 0

import codewars_test as test
# test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')

# test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
# test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')