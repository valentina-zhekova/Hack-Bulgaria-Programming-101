def reduce_file_path(path):
    if path[0] == '/':
        result = path.split('/')
        result = list(filter(lambda x: x != '' and x != '.', result))

        index = 0
        while index < len(result):
            if result[index] == ".." and index == 0:
                result.pop(index)
            elif result[index] == "..":
                result.pop(index - 1)
                result.pop(index - 1)
                index -= 1
            else:
                index += 1

        result = list(map(lambda x: "/" + x, result))
        if len(result) == 0:
            return "/"
        return "".join(result)
    return False
