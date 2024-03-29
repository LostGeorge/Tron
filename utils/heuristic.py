from tronproblem import TronProblem

barriers = set(['#', 'x', '1', '2'])

def action_move(loc, move):
    '''
    Helper function to get the coordinates of the result of an action
    '''
    if move == "U":
        return (loc[0] - 1, loc[1])
    elif move == "D":
        return (loc[0] + 1, loc[1]) 
    elif move == "L":
        return (loc[0], loc[1] - 1)
    elif move == "R":
        return (loc[0], loc[1] + 1)
    return loc


def determine_players(tron_state):
    if tron_state.ptm == 0:
        p1_loc = tron_state.player_locs[0]
        p2_loc = tron_state.player_locs[1]
    else:
        p1_loc = tron_state.player_locs[1]
        p2_loc = tron_state.player_locs[0]
    return [p1_loc, p2_loc]
    

def voronoi_heuristic(tron_state):
    '''
    Calculates the difference between "zones of control" as defined
    by a voronoi diagram--zones defining squares that can be reached by p1
    or p2 first.
    '''
    # We make it so that p1 is the player to move and p2 is opponent

    player_locs = determine_players(tron_state)
    p1_loc = player_locs[0]
    p2_loc = player_locs[1]

    board = tron_state.board

    p1_visited = set([p1_loc])
    p1_f = []
    p1_f.append(p1_loc)
    p2_visited = set([p2_loc])
    p2_f = []
    p2_f.append(p2_loc)

    while p1_f or p2_f:
        n_p1_f = []
        for loc in p1_f:
            moves = TronProblem.get_safe_actions(board, loc)
            for move in moves:
                next_loc = action_move(loc, move)
                if (next_loc not in p1_visited) and (next_loc not in p2_visited):
                    n_p1_f.append(next_loc)
                    p1_visited.add(next_loc)

        n_p2_f = []
        for loc in p2_f:
            moves = TronProblem.get_safe_actions(board, loc)
            for move in moves:
                next_loc = action_move(loc, move)
                if (next_loc not in p1_visited) and (next_loc not in p2_visited):
                    n_p2_f.append(next_loc)
                    p2_visited.add(next_loc)

        p1_f = n_p1_f
        p2_f = n_p2_f
    
    return len(p1_visited) - len(p2_visited)

def space_fill_heuristic(tron_state):
    count = 0
    
    for i in range(1, len(tron_state.board) - 2):
        for j in range(1, len(tron_state.board[0]) - 2):
            if tron_state.board[i][j] not in barriers:
                if tron_state.board[i][j+1] not in barriers:
                    count += 1
                if tron_state.board[i+1][j] not in barriers:
                    count += 1
    
    return count


def heuristic_func(tron_state):
    # Combine vornoi and space fill heuristics. Must be between 0 and 1 and account for player.
    x = len(tron_state.board) - 2
    y = len(tron_state.board[0]) - 2
    board_size = x * y
    board_space = 2 * (x - 1) * (y - 1)

    return space_fill_heuristic(tron_state)/board_space * \
        (voronoi_heuristic(tron_state) / board_size + 1)**2/4

