from Sudoku_Boardclass import board
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import Qt


#Setting up the board
gameboard=board(9)
lister=['600003005','903080000','051000600','000430007','008507100','400068000','007000980','000070402','800300006']
gameboard.setvalues(lister)

#Setting up the layout

def boardtogrid():
    for i in range(gameboard.size):
        for k in range(gameboard.size):
            if gameboard.b[k][i]==0:
                inboard=''
            else:
                inboard=str(gameboard.b[k][i])
            item=QTableWidgetItem(inboard)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            gameboard.table.setItem(k,i,item)

def reset():
    gameboard.setvalues(lister)




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
gameboard.SolveButton.clicked.connect(boardtogrid)
gameboard.Showbutton.clicked.connect(reset)
gameboard.Showbutton.clicked.connect(boardtogrid)

gameboard.layout.addWidget(gameboard.table)
gameboard.layout.addLayout(gameboard.hlay)


gameboard.hlay.addWidget(gameboard.SolveButton)
gameboard.hlay.addWidget(gameboard.Showbutton)

boardtogrid()
gameboard.window.setLayout(gameboard.layout)
gameboard.window.show()
gameboard.Game.exec_()


