
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



