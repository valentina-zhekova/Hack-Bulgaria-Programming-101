def simplify_fraction(fraction):
    divisors_nominator = divisors(fraction[0])
    divisors_denominator = divisors(fraction[1])
    common_divisors = list(filter(lambda x: divisors_nominator.count(x) != 0,
                           divisors_denominator))
    d = max(common_divisors)
    return (fraction[0] / d, fraction[1] / d)


def divisors(number):
    lst = []
    for div in range(1, number + 1):
        if number % div == 0:
            lst.append(div)
    return lst


def main():
    print("should be (1,3): %s" % simplify_fraction((3, 9)))
    print("should be (1,7): %s" % simplify_fraction((1, 7)))
    print("should be (2,5): %s" % simplify_fraction((4, 10)))
    print("should be (3,22): %s" % simplify_fraction((63, 462)))

if __name__ == '__main__':
    main()

# sudo apt-get install ...
# in cake: git
# ls -a --> ne barame skritata papka osven ako ne q triem
# subl .& --->
# git status
# git add ....
# git commit -m "........"
# git checkout .....
# git remote add origin ....shema....
