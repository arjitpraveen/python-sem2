class Complex:

    def initcomplex(self):
        self.realPart = int(input("Enter the real part: "))
        self.imgPart = int(input("Enter the imaginary part: "))

    def display(self):
        print(f"{self.realPart} + {self.imgPart}i", sep = "")

    def get_realPart(self):
        return self.realPart
    
    def get_imgPart(self):
        return self.imgPart
    
    def sum(self, c1, c2):
        self.realPart = c1.get_realPart() + c2.get_realPart()
        self.imgPart = c1.get_imgPart() + c2.get_imgPart()

c1 = Complex()
c2 = Complex()
c3 = Complex()

print("Enter the first complex number: ")
c1.initcomplex()
print("First complex number: ")
c1.display()


print("Enter the second complex number: ")
c2.initcomplex()
print("Second complex number: ")
c2.display()

print("Sum of the 2 complex numbers is: ")
c3.sum(c1, c2)
c3.display()
