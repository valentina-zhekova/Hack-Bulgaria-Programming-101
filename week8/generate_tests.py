# to fix ............

import sys

def make_class_name(word):


def main():

    dsl_file = open(sys.argv[1], "r")
    dsl_content = dsl_file.read().split('\n')
    dsl_file.close()

    generate_file_name = sys.argv[1][:-3] + "py"
    py_file = open(generate_file_name, "w")

    py_file.write("import unittest\n")

    imports_part = list(filter(lambda x:
                               x.split(" ")[1] == "from" or
                               x.split(" ")[1] == "import", dsl_content))

    py_file.write(("\n".join(imports_part) + "\n\n"))

    class_name = sys.argv[1][:-4]


if __name__ == '__main__':
    main()
