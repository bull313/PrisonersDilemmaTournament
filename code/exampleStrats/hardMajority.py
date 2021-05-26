def strategy(history, memory):
    choice = 1
    _, num_past_rounds = history.shape

    if num_past_rounds > 0:
        choice = round(sum(history[1]) / len(history[1]))

    return choice, None