def strategy(history, memory):
    choice = 1
    _, num_past_rounds = history.shape

    if num_past_rounds > 2:
        past_3_opp_moves = [ history[1, -3], history[1, -2], history[1, -1] ]

        if any([ move == 0 for move in past_3_opp_moves ]):
            choice = 0

    return choice, None