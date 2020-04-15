import funcs

def main(hand):
    #first, make dif_list(which is a hidden-tare)
    dif = make_dif(hand)
    #sols is a set of solutions(atari-hai)
    sols = set()

    #if the hand is chiitoi, add the wait for that to sols
    if funcs.chiitoi_wait(dif) < 13:
        sols.add(hand[funcs.chiitoi_wait(dif)])

    
