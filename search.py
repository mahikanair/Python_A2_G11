import random
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import time

class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _search(self, search_for):
        """Returns the index of the 'search_for' element contained
        in the _items property.
        
        Args:
            search_for: The element we are looking for in the list.
        
        Returns:
            int: Index of the 'search_for' element or -1 if not found.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self, search_for):
        self.time = 0
        return self.time


class LinSearch(Search):
    def _search(self, search_for):
        items = self.get_items()
        for i in range(len(items)):
            if items[i] == search_for:
                return i
        return -1

    def _time(self, search_for):
        start_time = time.time()
        lin_s = self._search(search_for)
        end_time = time.time()
        self.time = end_time - start_time
        return self.time


class BinSearch(Search):
    def _search(self, search_for):
        items = self.get_items()
        l = 0
        r = len(items) - 1
        while l <= r:
            mid = (r + l) // 2
            if items[mid] == search_for:
                return mid
            elif items[mid] < search_for:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def _time(self, search_for):
        start_time = time.time()
        sorted_items = self._search(search_for)
        end_time = time.time()
        self.time = end_time - start_time
        return self.time


if __name__ == '__main__':
  # Find the size vs time plots
  lin_t = []  # List to store the different amounts of time it took to do linear search (for different sizes)
  bin_t = []  # List to store the different amounts of time it took to do binary search (for different sizes)
  sizes = [10, 100, 500, 1000, 5000, 7500, 10000, 15000]  # Sizes for lists, up to 5000
  while True:  # Make sure the user gives the right input
      try:
          x = int(input('Enter a number to search for in the lists. If it is present, we will tell you the index at which it is found (starts at 0), else we will return -1.'))
          break
      except ValueError:
          print('Enter an integer input only!')

  for i in range(len(sizes)):
      # Creating random lists of the pre-defined sizes
      random_list = [random.randint(-1000, 1000) for i in range(sizes[i])]
      # Time taken for the searches with this particular random list
      lin = LinSearch(random_list)
      search_lin = lin._search(x)
      time_lin = lin._time(x)
      lin_t.append(time_lin)

      bin = BinSearch(sorted(random_list))
      search_bin = bin._search(x)
      time_bin = bin._time(x)
      bin_t.append(time_bin)

  # Plotting both in one graph to compare
  plt.plot(sizes, lin_t, color='red', label='Linear search timings')
  plt.plot(sizes, bin_t, color='blue', label='Binary Search timings')
  plt.xlabel('Sizes')
  plt.ylabel('Time')
  plt.title('Scatter Plot of Time taken to search vs. Size of list')
  plt.legend()

  # Save the plot to file (PNG format)
  plt.savefig('searches.png')

  # Show the plot
  plt.show()