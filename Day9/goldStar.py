from sys import argv


def getLastSubSerieElem(serie):
    subSerie = []
    isOnlyZeros = True
    for i in range(len(serie) - 1):
        subSerie.append(serie[i + 1] - serie[i])
        if subSerie[i] != 0:
            isOnlyZeros = False

    if not isOnlyZeros:
        subSerie.insert(0, subSerie[0] - getLastSubSerieElem(subSerie))
     
    return subSerie[0]


def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    myList = [line for line in open(filename)]

    sum = 0
    for line in myList:
        history = [int(element) for element in line.split()]
        lastSubElem = getLastSubSerieElem(history)
        historyPlus = history[0] - lastSubElem 

        sum += historyPlus
        
    print(sum)


if __name__ == "__main__":
    main()