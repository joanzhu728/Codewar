import codewars_test as test
import string

def pig_it(text):
    mylist = text.split()
    word = len(mylist)
    i = 0
    newlist = []
    output = ""

    while i < word:
        if mylist[i] != string.punctuation:
            newlist.append(mylist[i][1:] + mylist[i][:1] + "ay")
        else:
            newlist.append(mylist[i])
        i += 1
    
    i = 0
    while i < len(newlist) - 1:
        newlist[i] = newlist[i] +" "
        i += 1

    return output.join(newlist)

    # return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')