import sys
from random import randint


def main():
    file = open(sys.argv[1], "w")
    for i in range(int(sys.argv[2])):
        file.write(str(randint(1, 1000)) + ' ')
    file.close()

    # argument "r+" write, but don't fill content
    file = open(sys.argv[1], "r")
    content = file.read()
    print(content)
    file.close()
    print("\n")


if __name__ == '__main__':
    main()
