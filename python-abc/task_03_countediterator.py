#!/usr/bin/env python3


class CountedIterator:
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        
        Args:
            iterable: An iterable object (e.g., list, tuple).
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the current count of iterated items.
        
        Returns:
            int: The number of items that have been fetched so far.
        """
        return self.counter

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.
        
        Returns:
            The next item from the iterator.
        
        Raises:
            StopIteration: When there are no more items to fetch.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Return the iterator object itself.
        
        Returns:
            CountedIterator: The iterator object.
        """
        return self
