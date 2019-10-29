from tronproblem import TronState
from utils.heuristic import voronoi_heuristic, space_fill_heursitic

board = [['#', '#', '#', '#', '#', '#'],
         ['#', '2', '1', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', '#', '#', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', ' ', ' ', ' ', ' ', '#'],
         ['#', '#', '#', '#', '#', '#']]

player_locs = [(1,2), (1, 1)]

tron_st = TronState(board, player_locs, 1, {})

# print(voronoi_heuristic(tron_st))
print(space_fill_heursitic(tron_st))

