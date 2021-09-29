# encoding: utf-8

# EXERCÍCIO
# -----------------------------------
# Remover todos os 1 que estiverem na borda
# ou ligados à borda por algum outro elemento
# (horizontal ou vertical)
# -----------------------------------

import numpy as np

stateMatrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

def removeOnes(matrix):
    newMatrix = []

    for i in matrix:
        while ((i[0] == 1) or (i[-1] == 1)):
            if (i[0] == 1):
                i.remove(1)
                i.insert(0, 0)
            elif (i[-1] == 1):
                i.pop()
                i.append(0)
            else:
                break
        newMatrix.append(i)
    
    return newMatrix

def main():
    result = removeOnes(stateMatrix)
    print (np.array(result))

main()