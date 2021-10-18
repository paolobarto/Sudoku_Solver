import numpy as np
import os
here=os.path.dirname(os.path.abspath(__file__))
filename=os.path.join(here,'input.txt')
#using numpy to turn array of string to int
importedArr = []

with open(filename,'r') as f:

    for line in f.readlines():
        importedArr.append(line.split())
#grabs array from text file

arrar2d=[]
array2d=np.array(importedArr)
array2d=array2d.astype(int)


class Board:
    def __init__(self):
        self.array=array2d

    def printArr(self):
        print(self.array)

    def returnArr(self):
        return(self.array)

    def isEmpty(self,x,y):
        if self.array[x,y] == 0:
           return True
        else:
           return False

    def doesZeroExist(self):
        for j in range(0,9):
            for i in range(0,9):
                if self.array[j][i] == 0:
                    return True
        return False

    def outputAnswer(self):
        self.printArr()
        temp=str(self.array)

        with open("output,txt","w") as o:
                o.write(temp)

   