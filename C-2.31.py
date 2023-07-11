#Write a Python class that extends the Progression class so that each value in the progression is
#the absolute value of the difference between the pre- vious two values.
#You should include a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.



class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self.current = start
    
    def advance(self):
        """Update self.current to a new value.
        This should be overridden by a subclass to customize progression.
        By convention, if current is set to None, this designates the end of a finite progression.
        """
        self.current += 1
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current
            self.advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for _ in range(n)))


class AbsoluteDifference(Progression):
    def __init__(self, first=2,second=200):
        
        super().__init__(first)
        self.prev=second-first

    def advance(self):
        self.prev,self.current=self.current,abs(self.prev-self.current)


Progression=AbsoluteDifference()
Progression.print_progression(10)
