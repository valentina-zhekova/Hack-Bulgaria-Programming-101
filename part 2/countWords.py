def count_words(arr):
    dictionary = {}
    for word in arr:
        if not word in dictionary:
            dictionary[word] = arr.count(word)
    return dictionary


def main():
    print("should be {\'apple\': 2, \'pie\': 1, \'banana\': 1}: %s" %
          count_words(["apple", "banana", "apple", "pie"]))
    print("should be {\'ruby\': 1, \'python\': 3}: %s" %
          count_words(["python", "python", "python", "ruby"]))

if __name__ == '__main__':
    main()
