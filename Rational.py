import math

class Rational:
    def __init__(self, num, denom):
        """give a numerator and denominator for the rational number
        """
        self.numerator = num
        self.denominator = denom

    def __repr__(self):
        """print the frational representation
        """
        return str(self.numerator)+"/"+str(self.denominator)

    def __add__(self, other):
        """returns a rational that is this rational added to the passed rational
        """
        return Rational(self.numerator * other.denominator + self.denominator * other.denominator,\
                        self.denominator * other.denominator)
    def __eq__(self, other):
        """return equal to 
        """
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ge__(self, other):
        """return greater than or equal to
        """
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __str__(self):
        """return the string interpretation of the rational
        """
        return str(self.numerator)+"/"+str(self.denominator)

    def simplify(self):
        n = min(self.numerator, self.denominator)
        for i in range(n,1,-1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator /= i
                self.denominator /= i


r = Rational(2,12)
r.simplify()
print r