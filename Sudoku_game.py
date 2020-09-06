from Sudoku_Boardclass import board
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


#Setting up the board
gameboard=board(9)
gameboard.changeval(0,0,1)

#Setting up the layout
Game=QApplication([])
window=QWidget()
layout=QVBoxLayout()


table=QTableWidget(9,9)
for k in range(gameboard.size):
    table.setRowHeight(k,30)
    for i in range(gameboard.size):
        table.setItem(k,i, QTableWidgetItem(gameboard.b[k][i])) 
        table.setColumnWidth(i,30)
table.horizontalHeader().hide()
table.verticalHeader().hide()
table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
table.verticalScrollBar().setDisabled(True)
table.horizontalScrollBar().setDisabled(True)
# table.verticalScrollBar().hide()
# table.horizontalScrollBar().hide()
table.setFixedWidth(273)
table.setFixedHeight(273)

## Getting widgets and their connectionsA
SolveButton=QPushButton('Solve')
Showbutton=QPushButton('Show grid')

##connections
SolveButton.clicked.connect(gameboard.solve)
Showbutton.clicked.connect(gameboard.printboard)

layout.addWidget(table)
layout.addWidget(SolveButton)
layout.addWidget(Showbutton)

window.setLayout(layout)
window.show()
Game.exec_()


