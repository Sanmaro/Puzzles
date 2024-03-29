class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self._collection = collection
        self._items_per_page = items_per_page
        self._pages = [self._collection[i:i+self._items_per_page] 
                 for i in range(0, len(self._collection), self._items_per_page)]

    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self._collection)
    
    # returns the number of pages
    def page_count(self):
        return len(self._pages)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= len(self._pages):
            return -1
        return len(self._pages[page_index])
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self._collection):
            return -1
        return item_index // self._items_per_page


helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0) # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid