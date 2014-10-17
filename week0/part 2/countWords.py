def count_words(arr):
    dictionary = {}
    for word in arr:
        if not word in dictionary:
            dictionary[word] = arr.count(word)
    return dictionary
