from sys import argv
import re

def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    my_list = [line for line in open(filename)]

    cubeDict = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
        }

    sumLegalID = 0
    for i in range(len(my_list)):
        currGame = re.sub("Game \d: |Game \d\d: |Game \d\d\d: ", "", my_list[i])
        currGame = re.split(';|:', currGame)
        isCurrGameLegal = True
        
        for subGame in currGame:
            splitSubGame = re.sub(",", "", subGame)
            splitSubGame = splitSubGame.strip()
            splitSubGame = re.split(" ", splitSubGame)

            for y in range(0, len(splitSubGame), 2):
                if int(splitSubGame[y]) > cubeDict[splitSubGame[y + 1]]:
                    isCurrGameLegal = False
        
        if isCurrGameLegal:
            sumLegalID += i + 1

    print(sumLegalID)

if __name__ == "__main__":
    main()