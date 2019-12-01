from .heuristic import heuristic_func


def max_transition(asp, state, start_player, alpha=None, beta=None, cutoff=None, eval_f=None):
	if asp.is_terminal_state(state):
		return (asp.evaluate_state(state)[start_player], None)
	if cutoff != None:
		if cutoff == 0:
			return (eval_f(state), None)

	max_val = (float('-inf'), None)
	for action in asp.get_available_actions(state):
		new_state = asp.transition(state, action)
		if cutoff != None:
			value = min_transition(asp, new_state, start_player, alpha=alpha, beta=beta, cutoff=cutoff-1, eval_f=eval_f)[0]
		else:
			value = min_transition(asp, new_state, start_player, alpha=alpha, beta=beta)[0]
		if beta != None and value > beta:
			return (value, action)
		if value > max_val[0]:
			max_val = (value, action)
			if alpha != None:
				alpha = max(value, alpha)
	
	return max_val
		

def min_transition(asp, state, start_player, alpha=None, beta=None, cutoff=None, eval_f=None):
	if asp.is_terminal_state(state):
		return (asp.evaluate_state(state)[start_player], None)
	if cutoff != None:
		if cutoff == 0:
			return (eval_f(state), None)
	min_val = (float('inf'), None)
	for action in asp.get_available_actions(state):
		new_state = asp.transition(state, action)
		if cutoff != None:
			value = max_transition(asp, new_state, start_player, alpha=alpha, beta=beta, cutoff=cutoff-1, eval_f=eval_f)[0]
		else:
			value = max_transition(asp, new_state, start_player, alpha=alpha, beta=beta)[0]
		if alpha != None and value < alpha:
			return (value, action)
		if value < min_val[0]:
			min_val = (value, action)
			if beta != None:
				beta = min(value, beta)
	
	return min_val


def alpha_beta_cutoff(asp, cutoff_ply):
	start_state = asp.get_start_state()
	start_player = start_state.player_to_move()
	val, move = max_transition(asp, start_state, start_player, alpha=float('-inf'), beta=float('inf'),
		cutoff=cutoff_ply, eval_f=heuristic_func)

	return move

