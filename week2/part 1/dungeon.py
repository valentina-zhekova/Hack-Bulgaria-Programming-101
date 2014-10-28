class Dungeon:

    def __init__(self, filename):
        self.filename = filename

    def print_map(self):
        file = open(self.filename, "r")
        content = file.read()
        print(content)
        return True
