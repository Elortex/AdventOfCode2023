from sys import argv

def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    my_list = [line for line in open(filename)]

    print(my_list[1][139])

    sumOfPartNum = 0
    for x in range(len(my_list)):
        currentPartNumber = ''
        isPrevPosDigit = False
        isPartNumberVerified = False
        if isPartNumberVerified and not isPrevPosDigit:
            sumOfPartNum += int(currentPartNumber)

        for y in range(len(my_list[0])-1):
            if my_list[x][y].isdigit():
                currentPartNumber += my_list[x][y]

                for addX in range(-1, 1, 1):
                    for addY in range(-1, 1, 1):
                        try:
                            if {
                                my_list[x + addX][y + addY] != '.' and 
                                not my_list[x + addX][y + addY].isdigit()
                            }:
                                isPartNumberVerified = True
                        except:
                            pass
                isPrevPosDigit = True
            else:
                isPrevPosDigit = False
    print(sumOfPartNum)

if __name__ == "__main__":
    main()