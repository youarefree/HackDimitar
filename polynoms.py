class Addend:
    def __init__(self, coefficient, power):
        self.coefficient = int(coefficient)
        self.power = int(power)

    def get_coefficient(self):
        return self.coefficient

    def set_coefficient(self, coefficient):
        self.coefficient = coefficient

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power


class Polynom:
    def __init__(self, polynom):
        self.polynom = polynom
        self.addends = self.polynom.split("+")
        # init or main
        self.generate_addends()
        self.combine_addends()
        self.derivate = self.generate_derivates()

    def __str__(self):
        return "Polynom: {0}".format(self.polynom)

    def __repr__(self):
        return self.__str__()

    def generate_addends(self):
        result = []
        for addend in self.addends:  # KEY
            if addend.count("x") > 0:
                addend = addend.split("x")
                coefficient = addend[0]
                power = addend[1][1::]
                if coefficient is "":
                    coefficient = "1"
                if power is "":
                    power = "1"
                result.append(Addend(coefficient, power))
        self.addends = result

    def combine_addends(self):
        for i in range(len(self.addends)):
            for j in range(i + 1, len(self.addends)):
                if self.addends[i].get_power() == self.addends[j].get_power():
                    self.addends[i].set_coefficient(self.addends[i].get_coefficient() + self.addends[j].get_coefficient())
                    self.addends.pop(j)

    def generate_derivates(self):
        derivate = ""
        for addend in self.addends:
            derivate_coefficient = addend.get_coefficient() * addend.get_power()
            derivate_power = addend.get_power() - 1
            if derivate_coefficient is not 1:
                derivate += str(derivate_coefficient)
                if derivate_power > 0:
                    derivate += "*"
            if derivate_power > 0:
                derivate += "x"
            if derivate_power > 1:
                derivate += "^" + str(derivate_power)
            derivate += "+"
        return("f'(x) = " + derivate[:len(derivate) - 1:])


def main():
    polynom = Polynom('2x^3+3x+3x+1')
    print(polynom.derivate)

if __name__ == '__main__':
    main()
