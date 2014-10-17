import sys


def main():
    file = open(sys.argv[1], "r")
    content = file.read().split(" ")
    content = list(map(lambda x: int(x), content[:len(content) - 1]))
    print(sum(content))
    file.close()


if __name__ == '__main__':
    main()
