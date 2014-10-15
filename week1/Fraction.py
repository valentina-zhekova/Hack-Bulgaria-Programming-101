from fractions import gcd


class Fraction:
# immutable?????

    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __eq__(self, other):
        return (self.nominator * other.denominator ==
                other.nominator * self.denominator)

    def __lt__(self, other):
        return (self.nominator * other.denominator <
                other.nominator * self.denominator)

    def __gt__(self, other):
        return (self.nominator * other.denominator >
                other.nominator * self.denominator)

    def __add__(self, other):
        d = self.__lcm(other.denominator)
        return Fraction(self.nominator * (d // self.denominator) +
                        other.nominator * (d // other.denominator),
                        d)

    def __sub__(self, other):
        d = self.__lcm(other.denominator)
        return Fraction(self.nominator * (d // self.denominator) -
                        other.nominator * (d // other.denominator),
                        d)

    def __lcm(self, denom):
        return (self.denominator * denom) // gcd(self.denominator, denom)

    def __str__(self):
        return "(%s, %s)" % (self.nominator, self.denominator)

a = Fraction(2, 3)
b = Fraction(4, 5)
print(a + b)
