########################################################################
#### Course: Python Data Structures: Stacks, Queues, and Deques     ####
#########################################################################


class Deque:
    """
    Double End Queue
    FIFO and LIFO
    We are using a List as the base of our Deque. You can add and remove element from both sides
    At any separation of a Deque we have on the ledt side a Queue and at the right side a Stack
    The List[0] is the Front (left Side) and the List[-1] is the Rear (Right Side)
    """

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """
       This method adds an Item to the Front of the Deque
       The runtime for this method is O(n) - linear- because will end up shifting all indexes from the list to the
       right, which is a O(n) runtime.
       :return: None
       """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        :return void
        This method adds an Item to the Rear of the Deque
        The runtime for this method is O(1).
                """
        self.items.append(item)

    def remove_front(self):
        """
        This method removes and return the Left element in the List, which is a O(n) runtime because will end up
        shifting all indexes from the list to the left, which is a O(n) runtime.
        :return: Item
        """
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """
        This method removes and return the Right element in the List, which is a O(1) runtime.
        :return: Item
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """
       Returns (without Remove) the First item from the list that is the front of our Deque.
       The runtime for this method is O(1).
       """
        if self.items:
            return self.items[0]

        return None

    def peek_rear(self):
        """
       Returns (without Remove) the Last item from the list that is the Rear of our Deque.
       The runtime for this method is O(1).
       """
        if self.items:
            return self.items[-1]

        return None

    def is_empty(self):
        """
        :return True if the Deque is empty and False if not
        The runtime for this method is O(1).
        """
        return self.items == []

    def size(self):
        """
        Returns the size of the Deque.
        The runtime for this method is O(1).
        """
        return len(self.items)



