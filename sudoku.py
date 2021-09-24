from board import Board
from square import Square



#test=Board()
#print(test.isEmpty(0,0))
#test.printArr()

printTest=Square(0,0)
#With this object created, we are now able to create an object for each open square.
#We are able to use the square.findValidNumbers() member function to check the possible
#values of each open square.
#I will be able to create the object for each square and delete it once solved, when a 
#square is filled I will be able to refresh the values of each open square and eventually
#fully solve the board.

#The [8] value returend is the correct value and supports the position that the logic
#within the connection of classes is correct.

print(printTest.findValidNumbers())