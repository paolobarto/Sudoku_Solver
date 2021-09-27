import numpy as np
from board import Board
from squareVal import findSquareVal,possibleValue


    

class Square(Board):
    def __init__(self,x,y):
        self.x=x
        self.y=y

        Board.__init__(self)
        self.value=self.array[x][y]
        #This will be used to grab the array at each column, row, and box.
        self.row=(self.array[x])
        self.column=([row[y] for row in self.array])
        self.box=(findSquareVal(x,y,self.array))
        #^this is used to contain the entire array of the row,col,box

        self.possibleRow=possibleValue(self.row)
        self.possibleColumn=possibleValue(self.column)
        self.possibleBox=possibleValue(self.box)
        #^this is used to contain the values of the possible values in each area

    def setVal(self,val):
        self.value=val
        self.array[self.x][self.y]=val


    def printRow(self):
        print(self.row)

    def printColumn(self):
        print(self.column)

    def printBox(self):
        print(self.box)

    def returnValue(self):
        return self.value

    def findValidNumbers(self):
        isPres=bool
        tempArr=[]
        finalArr=[]

        for a in range(len(self.possibleRow)):
            isPres=False
            
            for b in range(len(self.possibleColumn)):
                    if self.possibleRow[a] is self.possibleColumn[b]:
                        isPres=True
                        break
            if isPres is True:
                tempArr.append(self.possibleRow[a])
        
        isPres=False
        for c  in range(len(tempArr)):
            isPres=False
            
            for d in range(len(self.possibleBox)):
                if tempArr[c] is self.possibleBox[d]:
                    isPres=True
            if isPres is True:
                finalArr.append(tempArr[c])
        return finalArr

    def validToInt(self):
        temp=self.findValidNumbers()
        temp=map(str,temp)
        temp=''.join(temp)
        temp=int(temp)

        self.setVal(temp)

