def strategy(history, memory):
    choice = 1

    if memory is not None:
        choice = 0
        memory = None
    elif history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
        memory = True
        
    return choice, memory