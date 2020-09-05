
# Printboard function

class board:

    def __init__(self,size):
        self.size=size
        self.b= [[0 for k in range(size)] for k in range(size)] 

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

    def reset(self):
        self.b= [[0 for k in range(self.size)] for k in range(self.size)] 
    
    def find_empty(self):
        for k in range(self.size):
            for i in range(self.size):
                if self.b[k][i]==0:
                    return k,i
        return None
