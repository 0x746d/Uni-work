# Tatu Matias Tuominen
# Student ID: 27475026
# FIT1045, Assignment 2, Task 2
# Sort algorithms are implemented from selection sorts in FIT1045 lecture slides


# returns list with records in list
# returns list, with each index representing title, artist, genre and price
# for loop runs through each line in given file and parses it to separate different elements
# returns list with each line in a list
def createDataBase():
    data = open('CD_store.txt')

    cdList = []
    for line in data:
        dataList = []

        data = line.strip().split('\t')

        comma1 = data[0].index(',')
        title = data[0][:comma1]
        comma2 = data[0].index(',', comma1 + 1)
        comma3 = data[0].index(',', comma2 + 1)
        artist = data[0][comma1 + 1:comma2]
        genre = data[0][comma2 + 1:comma3]
        price = float(data[0][comma3 + 1:])

        dataList.append(title)
        dataList.append(artist)
        dataList.append(genre)
        dataList.append(price)

        cdList.append(dataList)

    return cdList

listOfCds = (createDataBase())


# Helper function used in printList
# Finds title with the longest name
def longestTitleName(cdList):

    maxTitle = cdList[0][0]

    for i in range(1, len(cdList)):
        if len(cdList[i][0]) > len(maxTitle):
            maxTitle = cdList[i][0]

    return maxTitle

longestTitle = longestTitleName(createDataBase())


# Helper function used in printList
# Finds artist with the longest name
def longestArtistName(cdList):
    maxArtist = cdList[0][1]

    for i in range(1, len(cdList)):
        if len(cdList[i][1]) > len(maxArtist):
            maxArtist = cdList[i][1]

    return maxArtist

longestArtist = longestArtistName(createDataBase())


# Helper function used in printList
# Finds genre with longest name
def longestGenreName(cdList):

    maxGenre = cdList[0][2]

    for i in range(1, len(cdList)):
        if len(cdList[i][2]) > len(maxGenre):
            maxGenre = cdList[i][2]

    return maxGenre

longestGenre = longestGenreName(createDataBase())


# Sorts CDs by titles using selection sort
# Compares values and swaps them to arrange the rearrange the list
def SortByTitle(cdList):
    listLength = len(cdList)

    for x in range(listLength - 1):
        minPosition = x

        for y in range(x + 1, listLength):
            if cdList[y][0] < cdList[minPosition][0]:
                minPosition = y

        temp = cdList[x]
        cdList[x] = cdList[minPosition]
        cdList[minPosition] = temp
    listOfCds = cdList
    return cdList


# Sorts CDs by genre using selection sort
# Compares values and swaps them to arrange the rearrange the list
def SortByGenre(cdList):
    listLength = len(cdList)

    for x in range(listLength - 1):
        minPosition = x

        for y in range(x + 1, listLength):
            if cdList[y][2] < cdList[minPosition][2]:
                minPosition = y

        temp = cdList[x]
        cdList[x] = cdList[minPosition]
        cdList[minPosition] = temp
    listOfCds = cdList
    return cdList


# Sorts CDs by artist using selection sort
# Compares values and swaps them to arrange the rearrange the list
def SortByArtist(cdList):
    listLength = len(cdList)

    for x in range(listLength - 1):
        minPosition = x

        for y in range(x + 1, listLength):
            if cdList[y][1] < cdList[minPosition][1]:
                minPosition = y

        temp = cdList[x]
        cdList[x] = cdList[minPosition]
        cdList[minPosition] = temp
    listOfCds = cdList
    return cdList


# Sorts CDs by price in ascending order using selection sort
# Compares values and swaps them to arrange the rearrange the list
def SortByPrice(cdList):
    listLength = len(cdList)

    for x in range(listLength - 1):
        minPosition = x

        for y in range(x + 1, listLength):
            if cdList[y][3] < cdList[minPosition][3]:
                minPosition = y

        temp = cdList[x]
        cdList[x] = cdList[minPosition]
        cdList[minPosition] = temp
    listOfCds = cdList
    return cdList

# Goes through index 0 in each list
# appends item to targetList if entered string matches title
# checks if no titles were found, if targetList has an item in it it gets printed
def FindByTitle(targetString, listOfCds):

    targetList = []

    for i in range(len(listOfCds)):
        if targetString == (listOfCds[i][0]).lower():
            targetList.append(listOfCds[i])

    if len(targetList) == 0:
        print("\nNo CDs found for the title: {}\n".format(targetString))
    else:
        PrintList(targetList)

# Identical to FindByTitle, but checks index 1 in each list
def FindByArtist(targetString, listOfCds):
    targetList = []

    for i in range(len(listOfCds)):
        if targetString == (listOfCds[i][1]).lower():
            targetList.append(listOfCds[i])

    if len(targetList) == 0:
        print("\nNo CDs found by the artist: {}\n".format(targetString))
    else:
        PrintList(targetList)

# Identical to FindByTitle, but checks index 2 of each list
def FindByGenre(targetString, listOfCds):
    targetList = []

    for i in range(len(listOfCds)):
        if targetString == (listOfCds[i][2]).lower():
            targetList.append(listOfCds[i])

    if len(targetList) == 0:
        print("\nNo CDs found for the genre: {}\n".format(targetString))
    else:
        PrintList(targetList)

# Similar to other find functions
# Compares given dollar amount to items in index 3 of each list in list
# appends CD to targetList if it less than or equal to targetPrice
def FindByPrice(targetPrice, listOfCds):
    targetList = []

    for i in range(len(listOfCds)):
        if targetPrice >= float((listOfCds[i][3])):
            targetList.append(listOfCds[i])

    if len(targetList) == 0:
        print("\nNo CDs priced under ${:.2f}\n".format((targetPrice)))
    else:
        PrintList(targetList)

# uses longest item in each index place for each list in cdList
# longest items are used to format list
def PrintList(cdList):

    lenTitle = len(longestTitleName(cdList))
    lenArtist = len(longestArtistName(cdList))
    lenGenre = len(longestGenreName(cdList))
    header = ("{:<{}} {:<{}} {:<{}} {:^15}".format("Title", lenTitle+5, "Artist", lenArtist+5, "Genre", lenGenre+5, "Price"))
    headerLine = ("=" * len(header))
    print(header+"\n"+headerLine)

    for cd in cdList:
        print("{:<{}}| {:<{}}| {:<{}}| {:^15}".format(cd[0], lenTitle+5, cd[1], lenArtist+5, cd[2], lenGenre+5, "$" + str(cd[3])))
        print("-"*len(header))


# Function for navigating and viewing items in CD_store
# numbers are formatted to be right-aligned
# Function to be performed called based on number inputted by user
# ans variable initiated as empty string to enter while loop
def displayMenu():
    ans = " "

    while ans != "quit":
        print("{:^26}".format("MENU"))
        print("="*26)
        print("Enter Number of Function")
        print("{:>3} Print List of CDs ".format("1."))
        print("{:>3} Sort CDs by Title".format("2."))
        print("{:>3} Sort CDs by Artist ".format("3."))
        print("{:>3} Sort CDs by Genre".format("4."))
        print("{:>3} Sort CDs by Price ".format("5."))
        print("{:>3} Find All CDs by Title".format("6."))
        print("{:>3} Find All Cds by Artist".format("7."))
        print("{:>3} Find All CDs by Genre".format("8."))
        print("{:>3} Find All CDs by Price at Most X".format("9."))
        ans = input("10. Quit\n>>> ")
        if ans == "1":
            PrintList(listOfCds)
        elif ans == "2":
            SortByTitle(listOfCds)
        elif ans == "3":
            SortByArtist(listOfCds)
        elif ans == "4":
            SortByGenre(listOfCds)
        elif ans == "5":
            SortByPrice(listOfCds)
        elif ans == "6":
            targetString = (input("Enter name of title: ")).lower()
            FindByTitle(targetString, listOfCds)
        elif ans == "7":
            targetString = (input("Enter name of artist: ")).lower()
            FindByArtist(targetString, listOfCds)
        elif ans == "8":
            targetString = (input("Enter name of genre: ")).lower()
            FindByGenre(targetString, listOfCds)
        elif ans == "9":
            targetPrice = float(input("Enter a maximum price: $"))
            while targetPrice <= 0:
                targetPrice = float(input("Enter a valid price: $"))

            FindByPrice(targetPrice, listOfCds)
        elif ans.lower() == "10":
            quit()


# Start program by running display menu
displayMenu()

