from Sudoku_Boardclass import board

gameboard=board(9)
gameboard.changeval(0,0,1)
gameboard.printboard()
print(gameboard.valid(0,1,2))
print(gameboard.valid(0,1,1))