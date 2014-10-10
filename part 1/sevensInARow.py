def sevens_in_a_row(arr, n):
    count = 0
    for num in arr:
        if num == 7:
            count += 1
            if count == n:
                return True
                break
        elif count != 0:
            count = 0
    return False

# Ctrl + D -> all at once


print("should be True: %s" %
      sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
print("should be False: %s" % sevens_in_a_row([1, 7, 1, 7, 7], 4))
print("should be True: %s" %
      sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
print("should be True: %s" % sevens_in_a_row([7, 2, 1, 6, 2], 1))
