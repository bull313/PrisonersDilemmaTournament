from random import uniform

def strategy(history, memory):
    choice = 1
    if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        random_val = uniform(0, 1)

        if random_val > 0.25:
            choice = 0

    return choice, None