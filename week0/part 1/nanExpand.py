def nan_expand(times):
    if times == 0:
        return ""
    else:
        return "Not a " * times + "NaN"


def main():
    print("should be \"\": %s" % nan_expand(0))
    print("should be \"Not a NAN\": %s" % nan_expand(1))
    print("should be \"Not a Not a NAN\": %s" % nan_expand(2))
    print("should be \"Not a Not a Not a NAN\": %s" % nan_expand(3))

if __name__ == '__main__':
    main()
