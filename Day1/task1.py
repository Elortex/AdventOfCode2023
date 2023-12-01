from sys import argv
from functools import reduce

def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    my_list = [line for line in open(filename)]
    
    sum = 0
    for record in my_list:
        firstDig = ''
        lastDig = ''
        for i in range(len(record)):
            if record[i].isdigit() and (firstDig == ''):
                firstDig = record[i]
            if record[-i-1].isdigit() and (lastDig == ''):
                lastDig = record[-i-1]
        currentNumber = firstDig + lastDig
        print(currentNumber)
        sum += int(currentNumber)

    print(sum)


if __name__ == "__main__":
    main()