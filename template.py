from sys import argv
from functools import reduce

def main():
    if len(argv) < 2:
        print(f"Usage: {argv[0]} <file_name>")
        exit(1)
    filename = argv[1]
    my_list = [line for line in open(filename)]

if __name__ == "__main__":
    main()