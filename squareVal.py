def findSquareVal(row,column,arr):
    temparr=[0]*9
    n=0
    rowVal=0
    if column<3:
        columnVal=0
    elif column>2 and column<6:
        columnVal=3
    elif column>5:
        columnVal=6

    if(row<3):
        rowVal=0
    elif (row<6 and row>2):
            rowVal=3
    elif (row>5):
            rowVal=6
    
    for i in range(rowVal,rowVal+3):
        for a in range(columnVal,columnVal+3):
            temparr[n]=arr[i][a]
            n=n+1
    return temparr



def possibleValue(array):
    numberlist={1,2,3,4,5,6,7,8,9}
    temp=set(array)
    temp=numberlist.difference(temp)
    return list(temp)
    



