class Search(ABC):
    """Abstract base class for sorting."""

    def init(self, items):
        self._items = items

    @abstractmethod
    def _search(self, search_for):
        """Returns the 'search_for' element  contained
        in the _items property.
        Args:
            search_for: The element we are looking for in the list
        Returns:
            int: index of search_for element
        """
        pass

    def get_items(self):
        return self._items

    def _time(self, search_for):
      self.time = 0
      return self.time

      
class Linear(Search):
    def _search(self, search_for):
      items = self.get_items()
      n = len(items)
      for i in range(n):
        if items[i] == search_for:
            return i
      return -1
    def _time(self, search_for):
      start_time = time.time()
      lin_s = self._search(search_for)
      end_time = time.time()
      self.time = end_time - start_time
      return self.time