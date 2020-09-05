
# Printboard function

class board:

    def __init__(self,size):
        self.size=size
        self.b= [[0 for k in range(size)] for k in range(size)]

    def changeval(self,x,y,val):
        self.b[x][y]=val

    def printboard(self):
        stringboard = self.b
        for k in range(len(stringboard)):
            for i in range(len(stringboard)):
                temp = self.b[k][i]
                stringboard[k][i] = "{}".format(temp)
        for k in range(len(stringboard)):
            if k == 0:
                print("------------------")
            row = ''
            for i in range(len(stringboard)):
                if i % 3 == 0:
                    row += '| '
                row += stringboard[k][i]+' '
                if i == len(stringboard):
                    row += '| '
            print(row)
            if ((k+1) % 3 == 0 and k != 0) or k == len(stringboard):
                print("------------------")


gameboard=board(9)
gameboard.printboard()
