import numpy as np

#here=os.path.dirname(os.path.abspath(__file__))
#filename=os.path.join(here,'input.txt')
#using numpy to turn array of string to int


#importedArr = []

# with open('input.txt','r') as f:

#     for line in f.readlines():
#         importedArr.append(line.split())
# #grabs array from text file

# arrar2d=[]
# array2d=np.array(importedArr)
# array2d=array2d.astype(int)


firstArr=[]
secondArr=[]
thirdArr=[]

with open("input.txt") as f:
    for  index, line in enumerate(f):
        if index<9:
            firstArr.append((line.split()))
        elif  index>9 and index<19:
            secondArr.append((line.split()))
        elif index>19:
            thirdArr.append((line.split()))
        
firstArr=np.array(firstArr)
firstArr=firstArr.astype(int)
secondArr=np.array(secondArr)
secondArr=secondArr.astype(int)
thirdArr=np.array(thirdArr)
thirdArr=thirdArr.astype(int)




class Board:
    

    def __init__(self):
        self.count=1
        self.array=firstArr
        self.secondArray=secondArr
        self.thirdArray=thirdArr
        if not self.doesZeroExist():
            self.count=self.count+1
        if not self.doesZeroExistinSecond():
            self.count=self.count+2
        


        if self.count == 2:
           self.array=self.secondArray
        if self.count == 4:
            self.array=self.thirdArray
       
        
        


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

    def doesZeroExistinSecond(self):
        for j in range(0,9):
            for i in range(0,9):
                if self.secondArray[j][i] == 0:
                   return True
        return False

    def outputAnswer(self):
        self.printArr()
        temp=str(self.array)

        with open("output.txt","w") as o:
                o.writelines(temp)

    def checkStatus(self):
        if  not self.doesZeroExist():
            self.outputAnswer()
            if self.array is firstArr:
                self.array=self.secondArray
                return True
            elif self.array is secondArr:
                self.array = self.thirdArray
                return True
            return False
        else:
            return True

    
        
class TimeOut(Exception):
    pass


#############################################################################

