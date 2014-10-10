def nth_fibbonacci(n):
    before1 = 1
    before2 = 1
    current = 0
    if n > 1 and n < 3:
        return 1
    for i in range(3, n + 1):
        current = before1 + before2
        before2 = before1
        before1 = current
    return current

# P8 --> syntax rules
# preferrence -> ... -> "tab size":4 & "translate tabs to spaces":true

print("from 1 should be 1: %s" % nth_fibbonacci(1))
print("from 2 should be 1: %s" % nth_fibbonacci(2))
print("from 3 should be 2: %s" % nth_fibbonacci(3))
print("from 10 should be 55: %s" % nth_fibbonacci(10))
