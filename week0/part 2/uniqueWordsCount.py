from countWords import count_words


def unique_words_count(arr):
    return len(count_words(arr))


def main():
    print("should be 3: %s" %
          unique_words_count(["apple", "banana", "apple", "pie"]))
    print("should be 2: %s" %
          unique_words_count(["python", "python", "python", "ruby"]))
    print("should be 1: %s" % unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    main()
