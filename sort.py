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
    

class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""
    def _sort(self):
      items = self.get_items()
      if len(items) <= 1:
        return items
        
      mid = len(items) // 2
      left = items[:mid]
      right = items[mid:]

      # Recursively sort both halves
      merge_sort_left = MergeSort(left) #we need to create an instance because this method takes no arguments.
      # Hence we need to create a new instane for the left and right separately 
      merge_sort_right = MergeSort(right)

      left = merge_sort_left._sort()
      right = merge_sort_right._sort()

      # Merge the sorted halves
      merged = self._merge(left, right)

      return merged

    def _merge(self, left, right):
        merged = []
    
    # Initialize two pointers, i and j
        i = j = 0

    # Compare elements from both lists and merge them in ascending order
        while i < len(left) and j < len(right):
        # If the element in the left list is smaller, append it to the merged list
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
        # If the element in the right list is smaller or equal, append it to the merged list
            else:
                merged.append(right[j])
                j += 1

    # If there are remaining elements in the left list, append them to the merged list
        while i < len(left):
            merged.append(left[i])
            i += 1

    # If there are remaining elements in the right list, append them to the merged list
        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


    def _time(self):
      start_time = time.time() #start time
      sorted_items = self._sort() #run the sort method 
      end_time = time.time() #stop time
      self.time = end_time - start_time #Time elapsed
      return self.time
    

