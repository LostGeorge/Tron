from tronproblem import TronState
from utils.heuristic import voronoi_heuristic

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

print(voronoi_heuristic(tron_st))

