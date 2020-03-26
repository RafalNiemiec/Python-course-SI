 #MergeSort

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

    return list


print(mergeSort([1,6,4,5,8,2,3,0,5,6,1, 56, 70, 34, 26, 11, -4, -5, 11]))


def sortTest(test):
    print("Tested array: ", test)
    print("Simple sort result: ", simpleSort(test))
    print("Merge sort result: ", mergeSort(test))
    print(100*"-")


sortTest([-100, 1, 50, 60, 70, 12, 12, 45, 43, 23, 22, 56, 8, 5, 2, 3])
sortTest([-3, -5, 6, 10, 5, 6, 10, 50, 20, 22, 10, 5, -1, 132, 193, 5, 0])
sortTest([0, -4.2, -1.6, -1, 4.1, 5.7, 3.2])