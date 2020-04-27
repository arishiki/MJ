import re

#make list of differences
#...a bit awkward to use zip to refer "next" element
def make_dif(list0):
    return ''.join([str(x[1]-x[0]) for x in zip(list0[:-1], list0[1:])])


def init_pattern_tree(pattern_list):
    #pattern_list is given by a list of patterns.
    #pattern is as such:
    #[pattern, machi, label]
    
    #pattern is a list of int which represents the form of pattern
    #example: for 23456 3-men wait, pattern is [0,1,2,3,4]

    #machi is a list of int which represents machi
    #example: for 23456 3-men pattern, machi is [-1, 2, 5]

    #label is a list which represents the form of pattern tree.
    #it's like universal decimal classification
    #but to let it more universal, it is a list, not a string.
    #more complicated pattern which evolves from the pattern with label l
    #has the label l.append(i) (i is associated in turn)
    #example:
    #pattern 23 has label [0]
    #pattern 23456 has label [0, 0]
    
    #remark:
    #for this program this may seem too elaborate,
    #but this is for fun and for future application.

    #thus, pattern_list is as below:
    #[[[0,1],[-1,2],[0]], [[0,1,2,3,4],[-1,2,5],[0, 0]]]

    tree = [[],[],[]]

    for pattern in pattern_list:
        tree_append(tree, pattern)

    return tree

def tree_append(tree, pattern):
    p = pattern[2].pop(0)
    if pattern[2]:
        tree_append(tree[2][p], pattern)
    else:
        tree[2].append(pattern)

#as regular, chiitoi must have 7 different pairs
#meaning that it doesn't contain 4 identical pies
def chiitoi_wait(hand):
    #returns an index iff hand is tempai of chiitoi.
    #(chiitoi can't have 4 identical pies)
    #returns 13 if it is not.
    
    list_count = [hand.count(x) for x in hand]
    if list_count.count(1) == 1 and list_count.count(2) == 6:
        return list_count.index(1)
    else:
        return 13



def list_remove_list(list0, list_rm):
    #return a list removed elements of list_rm from list0
    list_cp = list(list0)
    for i in list_rm:
        if i in list_cp:
            list_cp.remove(i)
    return list_cp
    

def is_all_ments(list):
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
        shunts = list[0]+1 in list and list[0]+2 in list
                             
        return (list[0] == list[2] and is_all_ments(list[3:])) \
            or (shunts and is_all_ments(list_remove_list(list, \
                                        [list[0], list[0]+1, list[0]+2])))
    else:
        return False
        
def analyze_machi_without_head(list, head, sols):
    #judges if the list waits for ataris without head.
    #it returns updated sols.
    #head is an integer(0 for null)

    if len(list) % 3 == 2:
        p1 = list[0]
        if p1+1 in list:
            if p1+2 in list:
                #if we take shunts away and the remainder was machi without
                #head, then the full body is also machi without head
                sols = sols | analyze_machi_without_head(list_remove_list(list, [p1, p1+1, p1+2]), \
                                           head, sols)

            sols_add = {x for x in {p1 - 1, p1 + 2} if x > 0 and x < 10} - sols
            if sols_add and is_all_ments(list_remove_list(list, [p1, p1+1])):
                sols = sols | sols_add

        if p1+2 in list:
            #example: from 2,2,3,4,4,5,6,7 we take 2,4 away
            #and the remainder is all_ments
            #so we add 3 to sols
            if not p1+1 in sols and \
               is_all_ments(list_remove_list(list, [p1, p1+2])):
                sols.add(p1+1)
        
        
        if list[1] == p1:
            if {head, p1} - sols and \
                is_all_ments(list_remove_list(list, [p1, p1])):
                #this is when the wait is shabo
                sols.add(head)
                sols.add(p1)

            if list.count(p1) >= 3:
                sols = sols | analyze_machi_without_head(list_remove_list(list, [p1, p1, p1]), \
                                                        head, sols)

        return sols

    else:
        return set()

def list_in_list(sub_list_or_itr, super_list):
    list_cp = list(super_list)
    for i in sub_list_or_itr:
        if not i in super_list:
            return False
        list_cp.remove(i)
    else:
        return True

def analyze_with_head(patern_tree, list0, sols):
    p1 = list0[0]
    b1 = False
    if not list_in_list(map(lambda x: p1+x, patern_tree[0]), list0):
        return False
    else:
        for pattern in pattern_tree[2]:
            b1 = analyze_with_head(pattern, list0, sols) or b1
    list_cp = list(list0)
    for pattern in patterns:
        for i in pattern[0]:
            if not p1 + i in list_cp:
                break

            list_cp.pop(p1 + i)
        else:
            hoge

def analyze_tanki_specific_pattern(list):
    pattern_tree = [[[0,1,2,3],[0,3],[[0,1,2,3,4,5,6],[0,3,6],[]]], [[0,0,0,1],[-1, 1, 2],[]], [[],[],[]]]
    p1 = list[0]