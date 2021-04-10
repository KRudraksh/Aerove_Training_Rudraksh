class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def display(self):
        print(str(self.r))
    
    def conjugate(self):
        self.i=-self.i

    def modulus(self):
        print(self.r*self.r + self.i*self.i)

    def add(self,a):
        return Complex(self.r+a.r, self.i+a.i)

    def subtract(self,b):
        return Complex(self.r-b.r, self.i-b.i)

    def multiply(self,c):
        return Complex(self.r*c.r - self.i*c.i, self.r*c.i + self.i*c.r)

    def inverse(self):
        inv = Complex(self.r, -self.i)
        inv.r=inv.r/(self.modulus)
        inv.i=inv.i/(self.modulus)
    

    


    