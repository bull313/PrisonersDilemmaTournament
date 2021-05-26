def strategy(history, memory):
    wronged = history.shape[1] >= 1 and history[1,-1] == 0

    if wronged:
        if memory is None:
            memory = list()

        memory += [0] * 4 + [1] * 2

    if memory and len(memory) > 0:
        choice = memory[0]
        memory.pop(0)
        return choice, memory
    else:
        return 1, memory
