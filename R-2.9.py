#R-2.9 Implement the     sub     method for the Vector class of Section 2.3.3,
#so that the expression u!v returns a new vector instance representing the 
#difference between two vectors.





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
    
    def add(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self,other):
        if len(self)!=len(other):
            raise ValueError('Dimensions must agree')
        result=Vector(len(self))
        for j in range (len(self)):
            result[j]=self[j]-other[j]

    
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

w = u.__sub__(v)
print(w) 
