from Sudoku_Boardclass import board
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import Qt


#Setting up the board
gameboard=board(9)


#Setting up the layout
for k in range(gameboard.size):
    gameboard.table.setRowHeight(k,30)
    for i in range(gameboard.size): 
        gameboard.table.setColumnWidth(i,30)
gameboard.table.horizontalHeader().hide()
gameboard.table.verticalHeader().hide()
gameboard.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
gameboard.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
gameboard.table.verticalScrollBar().setDisabled(True)
gameboard.table.horizontalScrollBar().setDisabled(True)
# table.verticalScrollBar().hide()
# table.horizontalScrollBar().hide()
gameboard.table.setFixedWidth(273)
gameboard.table.setFixedHeight(273)
# table.setDisabled(True)

## Getting widgets and their connections
##connections
gameboard.SolveButton.clicked.connect(gameboard.solve)
gameboard.SolveButton.clicked.connect(gameboard.boardtogrid)
gameboard.Showbutton.clicked.connect(gameboard.reset)


gameboard.layout.addWidget(gameboard.table)
gameboard.layout.addLayout(gameboard.hlay)


gameboard.hlay.addWidget(gameboard.SolveButton)
gameboard.hlay.addWidget(gameboard.Showbutton)

gameboard.reset()
gameboard.window.setLayout(gameboard.layout)
gameboard.window.show()
gameboard.Game.exec_()


