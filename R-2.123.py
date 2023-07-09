#Exercise R-2.12 asks for an implementation of     mul ,
#for the Vector class of Section 2.3.3, to provide support for the syntax v 3. Implement the  
#rmul     method, to provide additional support for syntax 3   v.



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
    
    def __mul__(self, scalar):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * scalar
        return result
    def __rmul__(self,scalar):
        return self*scalar
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self.coords == other.coords
    
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
    
    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self.coords)[1:-1] + ">"

u=Vector(5)
u[0]=3
u[1]=4
u[2]=5
u[3]=4
u[4]=3
scalar=4

v=scalar*u
print(v)
