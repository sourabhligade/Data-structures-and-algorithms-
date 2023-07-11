#The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator. Implement a
#class named ReversedSequenceIterator that serves as a reverse iterator for any Python sequence type. 
#The first call to next should return the last element of the sequence, the second call to next should
#return the second-to-last element, and so forth.





class SequenceIterator:
    """An iterator for any of Python's sequence types."""
    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self.seq = sequence  # keep a reference to the underlying data
        self.k = len(sequence) - 1  # will decrement to 0 on first call to next
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self.k >= 0:
            result = self.seq[self.k]
            self.k -= 1
            return result
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


sequence = [1, 2, 3, 4, 5]
iterator = SequenceIterator(sequence)

for element in iterator:
    print(element)
