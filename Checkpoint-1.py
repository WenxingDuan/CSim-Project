class Polynomial(object):
    def __init__(self, a):
        self.a = a
        # self.x = int(x)

    def printPolynomial(self):
        print("P(x)=", end="")
        for i in range(0, len(self.a)):
            if i == 0:
            #not print 'x' after the power 0 term
                if self.a[i] != 0:
                    print(self.a[i], end=" ")
                    #ignore the 0 terms

            if i == 1:
            #not print '^1' after the power 1 term
                if self.a[i] < 0:
                    print(self.a[i], "x", end="")
                if self.a[i] > 0:
                    print("+", self.a[i], "x", end="")
                    #put '+' in front of positive number and '-' on negetive number

            if i > 1:
                if self.a[i] < 0:
                    print(self.a[i], "x ^", i, end="")
                if self.a[i] > 0:
                    print(" +", self.a[i], "x ^", i, end=" ")

        print("\n")

#---------------------------------------------------

    def addPolynomial(self, other):
        outputObj = self
        if len(outputObj.a) < len(other.a):
        #add shorter polynomial to longer polynomial
            minLength = len(outputObj.a)
            for i in range(minLength):
                other.a[i] = outputObj.a[i] + other.a[i]
                outputObj.a = other.a

        else:
            minLength = len(other.a)
            for i in range(minLength):
                outputObj.a[i] = outputObj.a[i] + other.a[i]

        return outputObj


#---------------------------------------------------

    def deritives(self):
        outputObj = self
        outputObj.a.pop(0)
        #delete the constant term
        for i in range(1, len(outputObj.a) + 1):
            outputObj.a[i - 1] = outputObj.a[i - 1] * i
        return outputObj


#---------------------------------------------------

    def antiDerivatives(self, c):
        outputObj = self
        outputObj.a.insert(0, c)
        #add 'c' as constant term
        for i in range(1, len(outputObj.a)):
            outputObj.a[i] = outputObj.a[i] / i
        return outputObj


a = Polynomial([2, 0, 4, -1, 0, 6])
b = Polynomial([-1, -3, 0, 4.5])
print("Pa(x) :")
a.printPolynomial()
print("Pa(x) + Pb(x) :")
a.addPolynomial(b).printPolynomial()
print("First deritives of Pa(x) :")
a.deritives().printPolynomial()
print("Anti-deritives of Pa(x) :")
a.antiDerivatives(2).printPolynomial()
