import funcs
import sys

def main(hand):
    #sols is a set of solutions(atari-hai)
    sols = set()

    #9 means head(shabo)
    #pattern_head_fixed = funcs.init_pattern_tree([[[0, 1],[-1, 2],[0]],   [[0,2],[1],[1]], [[0,0],[0, 9],[2]]\
    #                                               [[0,1,2,3,4],[-1,2,5],[0, 0]], [[0,0,1,1,2,2,3,3],[0,3,9],[2,0]]])
    
    pattern_tanki = funcs.init_pattern_tree([[[0],[0],[0]], [[0,0,0,1],[-1,1,2],[0, 0]], [[0,1,2,3],[0,3],[0,1]], \
                                                      [[0,1,1,1],[-1,0,2],[0, 2]], [[0,1,2,3,4,5,6],[0,3,6],[0,1,0]]])

    #if the hand is chiitoi, add the wait for that to sols
    chiitoi = funcs.chiitoi_wait(hand)
    if chiitoi < 13:
        sols.add(hand[chiitoi])

    #first, fix atama and anaylze.
    for x in hand:
        if hand.count(x) > 1:
            sols = funcs.analyze_machi_without_head(funcs.list_remove_list(hand, [x, x]), x, sols)

    sols = funcs.analyze_tanki2(pattern_tanki, hand, sols)
    for x in sols:
        if x in hand and hand.count(x) == 4:
            sols.remove(x)

    return sols

l1 = sorted([int(x) for x in sys.argv[1:14]])
print(main(l1))