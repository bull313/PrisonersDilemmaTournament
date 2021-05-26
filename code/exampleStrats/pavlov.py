from random import uniform

TIT_FOR_TAT = 0
ALWAYS_DEFECT = 1
TIT_FOR_TWO_TATS = 2
SCORE_THRESHOLD = 2.51

pointsArray = [[1,5],[0,3]]

def run_strategy(strat, history, memory):
    if strat == TIT_FOR_TAT:
        choice = 1
        if history.shape[1] >= 1 and history[1,-1] == 0:
            choice = 0
        return choice, memory
    elif strat == ALWAYS_DEFECT:
        return 0, memory
    elif strat == TIT_FOR_TWO_TATS:
        choice = 1
        if history.shape[1] >= 2 and history[1,-2] == 0 and history[1, -1] == 0:
            choice = 0
        return choice, memory

def strategy(history, memory):
    _, num_past_rounds = history.shape

    if num_past_rounds < 6:
        return run_strategy(TIT_FOR_TAT, history, memory)
    else:
        if memory is not None and num_past_rounds % 6 == 0:
            average_score = 0

            for i in range(1, 7):
                my_move = history[0, -i]
                opp_move = history[0, -i]

                average_score += pointsArray[my_move][opp_move]
            
            average_score /= 6

            if average_score < SCORE_THRESHOLD:
                memory = None

        if memory is None:
            past_opp_moves = [ history[1, -i] for i in range(1, 7) ]
            num_defects = len([ True for move in past_opp_moves if move == 0 ])

            if num_defects == 0:
                memory = TIT_FOR_TAT
            elif num_defects > 4:
                memory = ALWAYS_DEFECT
            elif num_defects == 3:
                memory = TIT_FOR_TWO_TATS
            else:
                memory = ALWAYS_DEFECT
            
        return run_strategy(memory, history, memory)
