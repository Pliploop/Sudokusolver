from Sudoku_Boardclass import board

gameboard=board(9)
gameboard.changeval(0,0,1)
gameboard.printboard()
gameboard.solve()
gameboard.printboard()