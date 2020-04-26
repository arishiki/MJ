import funcs
import re
import sys

def main(hand):
    #sols is a set of solutions(atari-hai)
    sols = set()

    #if the hand is chiitoi, add the wait for that to sols
    if funcs.chiitoi_wait(funcs.make_dif(hand)) < 13:
        sols.add(hand[funcs.chiitoi_wait(funcs.make_dif(hand))])

    #first, fix atama and anaylze.
    for x in hand:
        if hand.count(x) > 1:
            sols = funcs.analyze_machi_without_head(funcs.list_remove_list(hand, [x, x]), x, sols)

    #TBD

    return sols

l1 = [int(x) for x in sys.argv[1:14]]
print(main(l1))