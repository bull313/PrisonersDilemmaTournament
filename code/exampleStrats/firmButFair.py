def strategy(history, memory):
    if memory is None:
        memory = 1

    choice = memory
    _, num_past_rounds = history.shape

    if num_past_rounds > 1:
        my_last_move = history[0, -1]
        last_opp_move = history[1, -1]

        if [ my_last_move, last_opp_move ] == [ 1, 0 ]:
            memory = 0
        elif [ my_last_move, last_opp_move ] == [ 0, 0 ]:
            memory = 1

    return choice, memory
