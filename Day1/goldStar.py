from sys import argv

def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    my_list = [line for line in open(filename)]

    wordDigits = {
        "one" : "o1e",
        "two" : "t2o",
        "three" : "t3e",
        "four" : "f4r",
        "five" : "f5e",
        "six" : "s6x",
        "seven" : "s7n",
        "eight" : "e8t",
        "nine" : "n9e"
    }

    for i in range(len(my_list)):
        for key in wordDigits:
            my_list[i] = my_list[i].replace(key, wordDigits[key])

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