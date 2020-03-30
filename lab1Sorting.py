from time import *
from random import *

def createArray(lenght):
    list = []
    for i in range(lenght):
        list.append(randint(-100, 100))
    return(list)


def mergeSort(list):
    if len(list) > 1:
        i, j, k = 0, 0, 0
        half = len(list)//2

        #dividing list on two equal parts
        firstPart = list[:half]
        secondPart = list[half:]

        #dividing on smaller parts and sorting each
        mergeSort(firstPart)
        mergeSort(secondPart)

        #Compare two parts of list
        while i < len(firstPart) and j < len(secondPart):
            if firstPart[i] < secondPart[j]:
                list[k] = firstPart[i]
                i += 1
            else:
                list[k] = secondPart[j]
                j += 1
            k += 1

        #Check to similar element
        while i < len(firstPart):
            list[k] = firstPart[i]
            i += 1
            k += 1

        while j < len(secondPart):
            list[k] = secondPart[j]
            j += 1
            k += 1

    return list[len(list)-3:len(list)+1]


#smallest element method

def simpleSort(list):
    for i in range(len(list)):
        smallInd = i       #position of smallest element

        for j in range(i + 1, len(list)):
            if list[smallInd] > list[j]:
                smallInd = j

        #swap lowest value with i element
        list[i], list[smallInd] = list[smallInd], list[i]

    return list[len(list)-3:len(list)+1]


def entryPoint(fullList, minimal):
    complete = []
    j = 0
    for i in range(len(fullList)):
        if fullList[i]>minimal:
            complete.append(i)
            j += 1
            if j >= 3:
                sortTest(complete)
    return(fullList)

def compareTime(lenght):
    list = createArray(lenght)
    time1 = time()
    simpleSort(list)
    time2 = time()
    simpleSort(list)
    time3 = time()
    print([['simple sort', time2-time1], ['merge sort', time3-time2]])


compareTime(100)
compareTime(1000)