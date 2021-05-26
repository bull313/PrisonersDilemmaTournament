def strategy(history, memory):
    choice = 0
    if history.shape[1] >= 1 and history[1,-1] == 1: # Choose to defect if and only if the opponent just defected.
        choice = 1
    return choice, None