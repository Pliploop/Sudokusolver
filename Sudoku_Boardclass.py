
# Printboard function

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QColor
import time

class board:

    def __init__(self,size):
        self.size=size
        self.b= [[0 for k in range(size)] for k in range(size)]
        self.Game=QApplication([])
        self.window=QWidget()
        self.layout=QVBoxLayout()
        self.table=QTableWidget(9,9)
        self.SolveButton=QPushButton('Solve')
        self.Showbutton=QPushButton('Reset')
        self.hlay=QHBoxLayout()
        self.lister=['600003005','903080000','051000600','000430007','008507100','400068000','007000980','000070402','800300006']
        self.indices=[]

    def get_size(self):
        return self.size
    
    def printboard(self):
        stringboard = [['' for k in range(self.size)] for k in range(self.size)] 
        for k in range(len(stringboard)):
            for i in range(len(stringboard)):
                temp = self.b[k][i]
                stringboard[k][i] = "{}".format(temp)
        for k in range(len(stringboard)):
            if k == 0:
                print("-------------------------")
            row = ''
            for i in range(len(stringboard)):
                if i % 3 == 0:
                    row += '| '
                row += stringboard[k][i]+' '
            row+='|'    
            print(row)
            if ((k+1) % 3 == 0 and k != 0) or k == len(stringboard):
                print("-------------------------")

    def changeval(self,x,y,k):
        self.b[x][y]=k

    def color(self,item):
        row=item.row()
        column=item.column()
        text=item.text()
        print(text)
        if self.valid(row,column,int(text)):
            item.setBackground(QColor(0,255,0))

        else:
            item.setBackground(QColor(255,0,0))
            
        if int(text)>9 or int(text)<1:
            item.setBackground(QColor(255,0,0))
        if text=='':
            item.setBackground(QColor(0,0,0))
            text='0'
        self.b[row][column]=int(text)

    def reset(self):
        self.table.blockSignals(True)
        self.indices=[]
        self.setvalues(self.lister) 
        self.boardtogrid()
        self.table.blockSignals(False)
    
    def find_empty(self):
        for k in range(self.size):
            for i in range(self.size):
                if self.b[k][i]==0:
                    return k,i
        return None

    def valid(self,x,y,number):
        #Checking row first:
        for i in range(self.size):
            if self.b[x][i]==number and i!=y:
                return False
        for k in range(self.size):
            if self.b[k][y]==number and k!=x:
                return False
        boxX=x//3
        boxY=y//3
        for k in range(boxX*3,boxX*3+3):
            for i in range(boxY*3,boxY*3+3):
                if self.b[k][i]==number and k!=x and y!=i:
                    return False
        return True
    
    def solve(self):
        
        self.table.blockSignals(True)
        find=self.find_empty()
        if not find:
            self.table.blockSignals(False)
            return True
        else:
            row,col=find
        for i in range(1,10):
            if self.valid(row,col,i):
                self.changeval(row,col,i)
                # self.printboard()
                
                if self.solve():
                    self.table.blockSignals(False)
                    return True
                self.changeval(row,col,0)
                # self.printboard()
                


    def setvalues(self,listt):
        result=[]
        for k in listt:
            stringlist=list(k)
            result.append(stringlist)
        for k in range(self.size):
            for i in range(self.size):
                self.b[k][i]=int(result[k][i])
                if int(result[k][i])!=0:
                    self.indices.append([k,i])

    def boardtogrid(self):
        self.table.blockSignals(True)
        for i in range(self.size):
            for k in range(self.size):
                if self.b[k][i]==0:
                    inboard=''
                else:
                    inboard=str(self.b[k][i])
                item=QTableWidgetItem(inboard)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if [k,i] in self.indices:
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                    font = QFont()
                    font.setBold(True)
                    item.setFont(font)
                    item.setBackground(QColor(227,227,227))
                    
                self.table.setItem(k,i,item)
        self.table.blockSignals(False)