def strategy(history, memory):
    choice = 1

    if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        if memory is None:
            memory = dict()
            memory["num_defects"] = 1
            memory["next_moves"] = list()
        else:
            memory["num_defects"] += 1

        memory["next_moves"] += [0] * memory["num_defects"] + [1] * 2

    if memory is not None and len(memory["next_moves"]) > 0:
        choice = memory["next_moves"][0]
        memory["next_moves"].pop(0)
    
    return choice, memory