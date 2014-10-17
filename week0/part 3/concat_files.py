import sys


def main():
    file1 = open("MEGATRON", 'a')
    for f in sys.argv[1:]:
        file2 = open(f, "r")
        content = file2.read()
        file1.write(content + "\n")
        file2.close()
    file1.close()


if __name__ == '__main__':
    main()
