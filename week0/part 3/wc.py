import sys


def main():
    file = open(sys.argv[2], "r")
    content = file.read()
    if sys.argv[1] == 'chars':
        print(len(content))
    elif sys.argv[1] == 'words':
        print(content.count(" ") +
              content.count("\n") +
              content.count("\t"))
    elif sys.argv[1] == 'lines':
        print(content.count("\n"))
    file.close()


if __name__ == '__main__':
    main()
