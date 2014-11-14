from fractions import gcd


class Fraction:
# immutable == when two fractions interact none of both change,
# the result is stored in third fraction?????

    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator

    def __eq__(self, other):
        return (self.__nominator * other.__denominator ==
                other.__nominator * self.__denominator)

    def __lt__(self, other):
        return (self.__nominator * other.__denominator <
                other.__nominator * self.__denominator)

    def __gt__(self, other):
        return (self.__nominator * other.__denominator >
                other.__nominator * self.__denominator)

    def __add__(self, other):
        d = self.__lcm(other.__denominator)
        return Fraction(self.__nominator * (d // self.__denominator) +
                        other.__nominator * (d // other.__denominator),
                        d)

    def __sub__(self, other):
        d = self.__lcm(other.__denominator)
        return Fraction(self.__nominator * (d // self.__denominator) -
                        other.__nominator * (d // other.__denominator),
                        d)

    def __lcm(self, denom):
        return (self.__denominator * denom) // gcd(self.__denominator, denom)

    def __str__(self):
        return "(%s, %s)" % (self.__nominator, self.__denominator)
