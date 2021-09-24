import numpy as np
def findSquareVal(row,column,arr):
    temparr=[0]*9
    if row < 3 and column < 3:
        temparr[0] = arr[0][0]
        temparr[1] = arr[0][1]
        temparr[2] = arr[0][2]
        temparr[3] = arr[1][0]
        temparr[4] = arr[1][1]
        temparr[5] = arr[1][2]
        temparr[6] = arr[2][0]
        temparr[7] = arr[2][1]
        temparr[8] = arr[2][2]
    if ((row < 6 and row>2) and (column < 3)):
    
        temparr[0] = arr[3][0]
        temparr[1] = arr[4][0]
        temparr[2] = arr[5][0]
        temparr[3] = arr[3][1]
        temparr[4] = arr[4][1]
        temparr[5] = arr[5][1]
        temparr[6] = arr[3][2]
        temparr[7] = arr[4][2]
        temparr[8] = arr[5][2] 
    if (row>6 and column < 3):
    
        temparr[0] = arr[6][0]
        temparr[1] = arr[7][0]
        temparr[2] = arr[8][0]
        temparr[3] = arr[6][1]
        temparr[4] = arr[7][1]
        temparr[5] = arr[8][1]
        temparr[6] = arr[6][2]
        temparr[7] = arr[7][2]
        temparr[8] = arr[8][2]
    
    #Left 3 boxes^
    if ((column < 6 and column>2) and (row < 3)):
    
        temparr[0] = arr[0][3]
        temparr[1] = arr[1][3]
        temparr[2] = arr[2][3]
        temparr[3] = arr[0][4]
        temparr[4] = arr[1][4]
        temparr[5] = arr[2][4]
        temparr[6] = arr[0][5]
        temparr[7] = arr[1][5]
        temparr[8] = arr[2][5]
    
    if ((column < 6 and column>2) and ((row > 2)and(row<6))):
    
        temparr[0] = arr[3][3]
        temparr[1] = arr[4][3]
        temparr[2] = arr[5][3]
        temparr[3] = arr[3][4]
        temparr[4] = arr[4][4]
        temparr[5] = arr[5][4]
        temparr[6] = arr[3][5]
        temparr[7] = arr[4][5]
        temparr[8] = arr[5][5]
    
    if ((column < 6 and column>2) and (row > 5)):
    
        temparr[0] = arr[6][3]
        temparr[1] = arr[7][3]
        temparr[2] = arr[8][3]
        temparr[3] = arr[6][4]
        temparr[4] = arr[7][4]
        temparr[5] = arr[8][4]
        temparr[6] = arr[6][5]
        temparr[7] = arr[7][5]
        temparr[8] = arr[8][5]
    
    #middle 3 boxes^
    if (row < 3 and column>5):
    
        temparr[0] = arr[0][6]
        temparr[1] = arr[1][6]
        temparr[2] = arr[2][6]
        temparr[3] = arr[0][7]
        temparr[4] = arr[1][7]
        temparr[5] = arr[2][7]
        temparr[6] = arr[0][8]
        temparr[7] = arr[1][8]
        temparr[8] = arr[2][8]
    
    if ((row > 2 and row < 6) and column > 5):
    
        temparr[0] = arr[3][6]
        temparr[1] = arr[4][6]
        temparr[2] = arr[5][6]
        temparr[3] = arr[3][7]
        temparr[4] = arr[4][7]
        temparr[5] = arr[5][7]
        temparr[6] = arr[3][8]
        temparr[7] = arr[4][8]
        temparr[8] = arr[5][8]
    
    if (row > 5 and column > 5):
    
        temparr[0] = arr[6][6]
        temparr[1] = arr[7][6]
        temparr[2] = arr[8][6]
        temparr[3] = arr[6][7]
        temparr[4] = arr[7][7]
        temparr[5] = arr[8][7]
        temparr[6] = arr[6][8]
        temparr[7] = arr[7][8]
        temparr[8] = arr[8][8]
    return temparr



def possibleValue(array):
    
    numberList = list(range(1,10))

    pres=bool
    answer=[]
    for a in range(9):
        pres=False

        for b in range(9):
            if numberList[a] == array[b]:
                pres = True
                break
        
        if pres is False:
            answer.append(numberList[a])
    return answer
