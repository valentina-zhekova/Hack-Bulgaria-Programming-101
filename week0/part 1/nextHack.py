def next_hack(n):
    # to be sure it will return the next, not the current:
    number = bin(n + 1)[2:len(bin(n + 1))]
    l = len(number) // 2
    begin_string = number[:l]
    middle = number[l]
    end_string = begin_string[::-1]
    if len(number) % 2 == 1 and middle == '1' and end_string < number[l + 1:]:
        # only in this case we can't reach the reversed beginning
        # because we have already passed it
        # and end_string contains at least one zero
        end_string = change_chars(end_string)
        begin_string = end_string[::-1]
    # unite the number
    number = begin_string + '1' + end_string
    return int(number, 2)


# help function to create the what should be end_string
def change_chars(str):
    # strings are immutable
    lst = list(map(lambda x: x, str))
    for i in range(len(lst)):
        if lst[i] == '1':
            lst[i] = '0'
        else:
            lst[i] = '1'
            break
    return ''.join(lst)


def main():
    print("should be 1: %s" % next_hack(0))
    print("should be 21: %s" % next_hack(10))
    print("should be 8191: %s" % next_hack(8031))

if __name__ == '__main__':
    main()
