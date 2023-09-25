from abc import ABC, abstractmethod
import time

class Sort(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time

class BubbleSort(Sort):
    """Class for BubbleSort implementation."""

    def _sort(self):
      items = self.get_items()
      n = len(items)
      for i in range(n - 1):
        for j in range(0, n - i - 1): #accounts for least number of itertions
          if items[j] > items[j + 1]: #to sort in ascending order
            items[j], items[j + 1] = items[j + 1], items[j]
      return items

    def _time(self):
      start_time = time.time() #start time
      sorted_items = self._sort() #run the sort method 
      end_time = time.time() #stop time
      self.time = end_time - start_time #tells us total time 
      return self.time
