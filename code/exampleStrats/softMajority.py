def strategy(history, memory):
    choice = 1
    _, num_past_rounds = history.shape

    if num_past_rounds > 0:
        choice = 0 if sum(history[1]) / len(history[1]) < 0.5 else 1

    return choice, None