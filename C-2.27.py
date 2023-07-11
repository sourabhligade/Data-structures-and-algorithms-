#In Section 2.3.5, we note that our version of the Range class has im- plicit support for iteration,
 #   due to its explicit support of both     len and     getitem     .
 #  The class also receives implicit support of the Boolean test, “k in r” for Range r. 
  #This test is evaluated based on a forward itera- tion through the range,
 # as evidenced by the relative quickness of the test 2 in Range(10000000) versus 9999999 in 
                                                                                                                                                                                                                                  Range(10000000). Provide a more efficient implementation of the     contains     method to determine 
                                                                                                                                                                                                                                  whether a particular value lies within a given range. The running time of your method should be independent of the length of the range                                                                                                                                                   The running time of your method should be independent of the length of the range





class Range:
    """A class that mimics the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics are similar to the built-in range class.
        """
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:  # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0,n)

        # calculate the effective length once
        self.length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support getitem
        self.start = start
        self.step = step

    def __len__(self):
        """Return the number of entries in the range."""
        return self.length

    def __getitem__(self, k):
        """Return the entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < self.length:
            raise IndexError("index out of range")

        return self.start + k * self.step
    def __contains__(self,item):
        if self.start>0:
            return self.start<= item <self.start+self.length*self.step
        else:
            return self.start>=item >self.start+self.length*self.step


my_range=Range(1,10,2)
print(5 in my_range)
