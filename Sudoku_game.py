from Sudoku_Boardclass import board

gameboard=board(9)
gameboard.printboard()
gameboard.changeval(0,0,1)
gameboard.printboard()
print(gameboard.find_empty())