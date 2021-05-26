INIT_TEST_MOVES = [ 1, 0, 0, 1, 1 ]

INIT_MODE = 0
ADAPT_MODE = 1
EXECUTE_MODE = 2

pointsArray = [[1,5],[0,3]]

def strategy(history, memory):
    choice = None

    if memory is None:
        memory = dict()
        memory["mode"] = INIT_MODE
        memory["best_move"] = list()
    
    if memory["mode"] == INIT_MODE:
        _, num_past_rounds = history.shape

        if num_past_rounds < len(INIT_TEST_MOVES):
            return INIT_TEST_MOVES[num_past_rounds], memory
        else:
            memory["mode"] = ADAPT_MODE

    if memory == ADAPT_MODE:
        move_checks = {
            "00": { "score": 0, "len": 0 },
            "01": { "score": 0, "len": 0 },
            "10": { "score": 0, "len": 0 },
            "11": { "score": 0, "len": 0 }
        }

        for i in range(len(num_past_rounds) - 1):
            my_moves = [ history[0, i], history[0, i + 1] ]
            opp_moves = [ history[1, i], history[1, i + 1] ]

            move_check_key = str(my_moves[0]) + str(my_moves[1])
            score = pointsArray[my_moves[0]][opp_moves[0]] + pointsArray[my_moves[1]][opp_moves[1]]

            move_checks[move_check_key]["score"] += score
            move_checks[move_check_key]["len"] += 1
        
        highest_score = 0
        memory["best_move"] = None

        for mc in move_checks.keys():
            score = move_checks[mc]["score"] / move_checks[mc]["len"]
            if score >= highest_score:
                highest_score = score
                memory["best_move"] = [ int(c) for c in mc ]

        memory["mode"] = EXECUTE_MODE

    if memory["mode"] == EXECUTE_MODE:
        choice = memory["best_move"][0]
        memory["best_move"].pop(0)

        if (len(memory["best_move"])) == 0:
            memory["mode"] = ADAPT_MODE

    return choice, memory
