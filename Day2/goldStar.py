from sys import argv
import re

def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    my_list = [line for line in open(filename)]

    sumLegalID = 0
    for i in range(len(my_list)):
        currGame = re.sub("Game \d: |Game \d\d: |Game \d\d\d: ", "", my_list[i])
        currGame = re.split(';|:', currGame)

        cubeDict = {
            'red' : 0,
            'green' : 0,
            'blue' : 0
        }

        for subGame in currGame:
            splitSubGame = re.sub(",", "", subGame)
            splitSubGame = splitSubGame.strip()
            splitSubGame = re.split(" ", splitSubGame)

            for y in range(0, len(splitSubGame), 2):
                if int(splitSubGame[y]) > cubeDict[splitSubGame[y + 1]]:
                    cubeDict[splitSubGame[y + 1]] = int(splitSubGame[y])

        sumLegalID += cubeDict["blue"] * cubeDict["green"] * cubeDict["red"]
        
    print(sumLegalID)
    
if __name__ == "__main__":
    main()