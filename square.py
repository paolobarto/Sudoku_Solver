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
        
        box=Box(self.x,self.y)
        self.box=(box.boxy)
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
        one=set(self.possibleRow)
        two=set(self.possibleColumn)
        three=set(self.possibleBox)
        one=(one.intersection(two)).intersection(three)
        return list(one)

    def validToInt(self):
        temp=self.findValidNumbers()
        temp=map(str,temp)
        temp=''.join(temp)
        temp=int(temp)

        self.setVal(temp)


#Added Class in Assingment 4, Although could be completed with direct logic, this allows for me
#to make more complicated code in the future
class Box(Board):
    def __init__(self,x,y):
        super().__init__()
        self.box=findSquareVal(x,y,self.array)
    def _get_box(self):
        return self.box

    boxy=property(_get_box)