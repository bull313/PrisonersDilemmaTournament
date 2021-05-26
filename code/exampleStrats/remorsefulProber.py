from random import uniform

def strategy(history, memory):
    choice = 1
    if (history.shape[1] >= 1 and history[1,-1] == 0) or uniform(0, 1) <= 0.1:
        choice = 0
    
    if history.shape[1] > 2:
        my_last_3_moves = [ history[0, -3], history[0, -2], history[0, -1] ]
        opp_last_3_moves = [ history[1, -3], history[1, -2], history[1, -1] ]

        past_3_turns_moves = my_last_3_moves + opp_last_3_moves

        if all([move == 0 for move in past_3_turns_moves]):
            choice = 1

    return choice, None
