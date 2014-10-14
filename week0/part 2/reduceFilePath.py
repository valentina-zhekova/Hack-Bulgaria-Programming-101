def reduce_file_path(path):
    result = path.split('/')
    result = list(filter(lambda x: x != '' and x != '.', result))

    index = 0
    while index < len(result):
        if result[index] == ".." and index == 0:
            result.pop(index)
        elif result[index] == "..":
            result.pop(index)
            result.pop(index - 1)
        else:
            index += 1

    result = list(map(lambda x: "/" + x, result))
    if len(result) == 0:
        return "/"
    return "".join(result)


def main():
    print("should be \"/\": %s" % reduce_file_path("/"))
    print("should be \"/\": %s" % reduce_file_path("/srv/../"))
    print("should be \"/srv/www/htdocs/wtf\": %s" %
          reduce_file_path("/srv/www/htdocs/wtf/"))
    print("should be \"/srv/www/htdocs/wtf\": %s" %
          reduce_file_path("/srv/www/htdocs/wtf"))
    print("should be \"/srv\": %s" % reduce_file_path("/srv/./././././"))
    print("should be \"/etc/wtf\": %s" % reduce_file_path("/etc//wtf/"))
    print("should be \"/\": %s" % reduce_file_path("/etc/../etc/../etc/../"))
    print("should be \"/\": %s" % reduce_file_path("//////////////"))
    print("should be \"/\": %s" % reduce_file_path("/../"))

if __name__ == '__main__':
    main()
