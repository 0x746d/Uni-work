# takes number of rows as input
# generates Pascal's triangle up to input number of rows
# Generates triangle using recursion

# validates that user input is a non-negative integer
def checkInput():
    number = -1
    while number < 0:
        number = int(input("Number n: "))

    return number



# takes list as input
# adds 1 to it if it's empty
# else updates current list to the next line of the triangle
# adds 1 to the end of each list
# returns updated list
def createRow(currentList):
    temp = []

    temp.append(1)
    if len(currentList) == 0:
        temp = [1]
    else:
        for i in range(0, len(currentList)-1):
            temp.append(currentList[i]+currentList[i+1])

        temp.append(1)
    return temp


# prints each integer in list
def printList(currentList):
    for num in currentList:
        print(num, end=" ")
    print("\n")


# current list as input
# recursively calls printPascal to generate n-1 list
def printPascal(currentList, n):
    if n == 0:
        currentList = createRow(currentList)
        printList(currentList)
        return currentList
    else:
        currentList = printPascal(currentList, n-1)
        currentList = createRow(currentList)
        printList(currentList)
        return currentList


printPascal([], checkInput())





