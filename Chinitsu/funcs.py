import re

#make list of differences
#...a bit awkward to use zip to refer "next" element
def make_dif(list0):
    return ''.join([str(x[1]-x[0]) for x in zip(list0[:-1], list0[1:])])

#as regular, chiitoi must have 7 different pairs
#meaning that it doesn't contain 4 identical pies
def chiitoi_wait(dif):
    #chiitoi_tempai must have 0, positive number repeats and
    #only one exceptional positive number.

    #if you come across the exception, you turn the "always_pair" switch off.
    #except for that, you switch 0, positive, 0, positive,...
    #we represent this by "expect_0" switch.

    #if you run out the dif list not meeting the exception to the 0-positive
    #switching,
    #that means you have chiitoi hand with the last pie being the wait.

    #this function returns the index of the wait of chiitoi hand.
    #if it isn't chiitoi, this returns 13, which is out of range.
    
    expect_0 = True
    always_pair = True
    candidate = 12
    for i in range(12):
        if expect_0:
            if dif[i]:
                if always_pair:
                    always_pair = False
                    candidate = i
                else:
                    return 13
            else:
                expect_0 = False
        else:
            if not dif[i]:
                return 13
            else:
                expect_0 = True

    return candidate

def shorten_list_from_dif(list, *args):

    #shorten the list by naming specific index of dif_str
    #example:
    #slfd([1,1,1,2,2,3,4,5], 2, 4) = [1,1,2,4,5]
    #when you want to exclude the 1,2,3 ments found by
    #its difference.
    
    start = 0
    result = []
    for i in range(len(args)):
        if i < len(args) - 1:
            result = result + list[start:args[i]]
            start = args[i] + 1
        else:
            result = result + list[start:args[i]] + list[args[i] + 2:]

    return result
    

def is_all_ments(list, str_dif):
    #we get stringfied version of dif because we want to
    #use regular expression.
    
    #is used for judging if the list is a set of ments(3 pies which is
    #either 3 identical pies or a sequence with each differences are
    #exactly 1's).
    #ofc, this list must be length of 3N.
    
    #if you have excluded all the ments and you have empty list,
    #then it is all ments.
    if not list:
        return True
    elif not len(list) % 3:
        m = re.match('0*(1)0*(1)', str_dif)
        if m:
            shortened_list = \
                shorten_list_from_dif(list, m.start(1), m.start(2))
            shortened_str_dif = make_dif(shortened_list)

        else:
            shortened_list = []
            shortened_str_dif = ''
                             
        return (str_dif[:2] == '00' and is_all_ments(list[3:], str_dif[3:])) \
            or (m and is_all_ments(shortened_list, shortened_str_dif))

    else:
        return False
        
