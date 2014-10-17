import sys


def main():
    for f in sys.argv[1:]:
        file = open(f, "r")
        content = file.read()
        print(content + "\n")
        file.close()


if __name__ == '__main__':
    main()
