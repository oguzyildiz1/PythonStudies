#linear searching algorithms
#source: https://www.geeksforgeeks.org/introduction-to-searching-data-structure-and-algorithm-tutorial/

import os

def findData(array1, searched):
    #we need iteration until the searched data found
    for i in range(len(array1)):
        if array1[i] == searched:
            return searched, i
    
    return

    #return the index


array1 = ["10","50","30","80","60","20","90","40"]

userInput = input("Aranan? ")

result = findData(array1, userInput)

if result:
    print(result, " bulundu")
else:
    print("no result found.")


