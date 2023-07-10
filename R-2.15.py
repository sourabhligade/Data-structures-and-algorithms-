#The Vector class of Section 2.3.3 provides a constructor that takes an in- teger d,
#and produces a d-dimensional vector with all coordinates equal to 0. Another convenient 
#form for creating a new vector would be to send the constructor a parameter that is some 
#iterable type representing a sequence of numbers, and to create a vector with dimension 
#equal to the length of that sequence and coordinates equal to the sequence values.
#For example, Vector([4, 7, 5]) would produce a three-dimensional vector with coordi- nates 
#<4, 7, 5>. Modify the constructor so that either of these forms is acceptable; that is, if a single 
#integer is sent, it produces a vector of that dimension with all zeros, 
#but if a sequence of numbers is provided, it pro- duces a vector with coordinates based on that sequence.





class Vector:
    """Represent a vector in a multidimensional space."""
    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self.coords = [0] * d
    
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self.coords)
    
    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self.coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self.coords[j] = val
    
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __radd__(self,other):
        if not isinstance(other,list):
            if len(self)!=len(other):
                raise ValueError('Dimensions must agree')
        result=Vector(len(self))
        for j in range(len(self)):
            result[j]=other[j]+self[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    
    def __mul__(self, other):
        if isinstance(self,Vector):
            if len(self)!=len(other):
                raise ValueError('dimensions do not match')
            dot_product=0
            for j in range(len(self)):
                dot_product+=self[j]*other[j]
            return dot_product
        elif isinstance(other,(int,float)):
            result=Vector(len(self))
            for j in range(len(self)):
                result[j]=self[j]*other
            return result
        else:
            raise TypeError("Unsupported operand type for multiplication.")


    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self.coords == other.coords
    
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
    
    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self.coords)[1:-1] + ">"

u = Vector(3)
u[0] = 1
u[1] = 2
u[2] = 3

v = Vector(3)
v[0] = 4
v[1] = 5
v[2] = 6

dot_product = u * v
print(dot_product)
