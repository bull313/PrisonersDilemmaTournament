from random import uniform

def soft_majority(history, memory):
	choice = 1
	_, num_past_rounds = history.shape

	if num_past_rounds > 0:
		choice = 0 if sum(history[1]) / len(history[1]) < 0.5 else 1

	return choice, None

def hard_majority(history, memory):
	choice = 1
	_, num_past_rounds = history.shape

	if num_past_rounds > 0:
		choice = round(sum(history[1]) / len(history[1]))

	return choice, None

TIT_FOR_TAT = 0
ALWAYS_DEFECT = 1
TIT_FOR_TWO_TATS = 2
SCORE_THRESHOLD = 2.51

pointsArray = [[1,5],[0,3]]

def run_strategy(strat, history, memory):
    if strat == TIT_FOR_TAT:
        choice = 1
        if history.shape[1] >= 1 and history[1,-1] == 0:
            choice = 0
        return choice, memory
    elif strat == ALWAYS_DEFECT:
        return 0, memory
    elif strat == TIT_FOR_TWO_TATS:
        choice = 1
        if history.shape[1] >= 2 and history[1,-2] == 0 and history[1, -1] == 0:
            choice = 0
        return choice, memory

def pavlov(history, memory):
	_, num_past_rounds = history.shape

	if num_past_rounds < 6:
		return run_strategy(TIT_FOR_TAT, history, memory)
	else:
		if memory is not None and num_past_rounds % 6 == 0:
			average_score = 0

			for i in range(1, 7):
				my_move = history[0, -i]
				opp_move = history[0, -i]

				average_score += pointsArray[my_move][opp_move]
			
			average_score /= 6

			if average_score < SCORE_THRESHOLD:
				memory = None

		if memory is None:
			past_opp_moves = [ history[1, -i] for i in range(1, 7) ]
			num_defects = len([ True for move in past_opp_moves if move == 0 ])

			if num_defects == 0:
				memory = TIT_FOR_TAT
			elif num_defects > 4:
				memory = ALWAYS_DEFECT
			elif num_defects == 3:
				memory = TIT_FOR_TWO_TATS
			else:
				memory = ALWAYS_DEFECT
			
		return run_strategy(memory, history, memory)

def gtft10(history, memory):
	choice = 1
	if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
		random_val = uniform(0, 1)

		if random_val > 0.1:
			choice = 0

	return choice, None

def gtft1(history, memory):
	choice = 1
	if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
		random_val = uniform(0, 1)

		if random_val > 0.01:
			choice = 0

	return choice, None

def gtft5(history, memory):
	choice = 1
	if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
		random_val = uniform(0, 1)

		if random_val > 0.05:
			choice = 0

	return choice, None

def gtft25(history, memory):
	choice = 1
	if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
		random_val = uniform(0, 1)

		if random_val > 0.25:
			choice = 0

	return choice, None

def gtft50(history, memory):
	choice = 1
	if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
		random_val = uniform(0, 1)

		if random_val > 0.50:
			choice = 0

	return choice, None

def gradual(history, memory):
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

def ftft(history, memory):
	choice = 1
	if history.shape[1] >= 2 and history[1,-1] == 0 and history[1,-2] == 0: # We check the TWO most recent turns to see if BOTH were defections, and only then do we defect too.
		choice = 0
	return choice, None

def tft(history, memory):
	choice = 1
	if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
		choice = 0
	return choice, None

def soft_grudger(history, memory):
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

def grim_trigger(history, memory):
	wronged = False
	if memory is not None and memory: # Has memory that it was already wronged.
		wronged = True
	else: # Has not been wronged yet, historically.
		if history.shape[1] >= 1 and history[1,-1] == 0: # Just got wronged.
			wronged = True

	if wronged:
		return 0, True
	else:
		return 1, False

def firm_but_fair(history, memory):
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

BETRAY = 0
COOPERATE = 1
ME = 0
OPPONENT = 1
LAST_MOVE = -1
NUM_ATTEMPTS_PER_STRAT = 20

TEST_STRATEGIES = 0
EVAL_STRATEGIES = 1
USE_BEST_STRATEGY = 2
strategy_state = TEST_STRATEGIES
best_strategy = None
best_strategy_name = None
strategies = [
	{
		"strategy": gtft10,
		"average_score": 0,
		"name": "gtft10"
	},
	{
		"strategy": gtft5,
		"average_score": 0,
		"name": "gtft5"
	},
	{
		"strategy": gtft1,
		"average_score": 0,
		"name": "gtft1"
	},
	{
		"strategy": gradual,
		"average_score": 0,
		"name": "gradual"
	},
	{
		"strategy": pavlov,
		"average_score": 0,
		"name": "pavlov"
	}
]
used_strategies = dict()

def strategy(history, memory):
	global best_strategy
	global best_strategy_name
	global strategy_state

	_, num_past_rounds = history.shape
	ret = None
	ret_name = ""

	if strategy_state == TEST_STRATEGIES:
		strat_idx = int(num_past_rounds // NUM_ATTEMPTS_PER_STRAT)
		strat_test_idx = num_past_rounds % NUM_ATTEMPTS_PER_STRAT

		if strat_idx <= len(strategies):

			strat = strategies[strat_idx] if strat_idx < len(strategies) else None
			
			if strat_test_idx == 0:
				memory = None

				if num_past_rounds > 0:
					prev_strat = strategies[strat_idx - 1]
					my_last_move = history[ME, LAST_MOVE]
					opp_last_move = history[OPPONENT, LAST_MOVE]
					prev_strat["average_score"] += pointsArray[my_last_move][opp_last_move] / NUM_ATTEMPTS_PER_STRAT

					if strat_idx == len(strategies):
						strategy_state = EVAL_STRATEGIES
			else:
				my_last_move = history[ME, LAST_MOVE]
				opp_last_move = history[OPPONENT, LAST_MOVE]
				strat["average_score"] += pointsArray[my_last_move][opp_last_move] / NUM_ATTEMPTS_PER_STRAT

			if strat is not None:
				ret = strat["strategy"](history, memory)
				ret_name = strat["name"]

	if strategy_state == EVAL_STRATEGIES:
		best_strategy = strategies[0]["strategy"]
		best_strategy_score = strategies[0]["average_score"]
		best_strategy_name = strategies[0]["name"]

		for i in range(1, len(strategies)):
			strat = strategies[i]

			if strat["average_score"] > best_strategy_score:
				best_strategy = strat["strategy"]
				best_strategy_score = strat["average_score"]
				best_strategy_name = strat["name"]

		strategy_state = USE_BEST_STRATEGY

	if strategy_state == USE_BEST_STRATEGY:
		ret = best_strategy(history, memory)
		ret_name = best_strategy_name

	if ret_name and ret_name not in used_strategies.keys():
		used_strategies.update({ ret_name: 1 })
	elif ret_name:
		used_strategies[ret_name] += 1

	print(used_strategies)

	return ret
