#Write a Python class that extends the Progression class so that each value in the progression is the square 
#root of the previous value. (Note that you can no longer represent each value with an integer.)
#Your construc- tor should accept an optional parameter specifying the start value, using 65,536 as a default.





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

class SquareRootProgressions(Progression):
    def __init__(self, first=65,second=536):
        super().__init__(first)
    def advance(self):
        self.current**=0.5

Progression=SquareRootProgressions()
Progression.print_progression(10)
        
