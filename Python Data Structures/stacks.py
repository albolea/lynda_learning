########################################################################
#### Course: Python Data Structures: Stacks, Queues, and Deques     ####
#########################################################################


class Stack:
    """
    LIFO
    We are using a List as the base of our Stack. The left Side of the List is the end (bottom) of our Stack and the
    right side is the Top of the Stack.
    """

    def __init__(self):
        """Constructor for Stack"""
        self.items = []

    def push(self, item):
        """
        :item Any data
        :return void
        Receives an item and appends it to the end of the list.
        The runtime for this method is O(1).
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last item from the list that is the top of our Stack.
        The runtime for this method is O(1).
        """
        if self.items:
            return self.items.pop()

        return None

    def peek(self):
        """
        Returns (without Remove) the last item from the list that is the top of our Stack.
        The runtime for this method is O(1).
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """
        Returns the size of the Stack.
        The runtime for this method is O(1).
        """
        return len(self.items)

    def is_empty(self):
        """
        :return True if the Stack is empty and False if not
        The runtime for this method is O(1).
        """
        return self.items == []


def match_symbols(symbol_str):
    symbol_pair = {'(': ')',
                   '[': ']',
                   '{': '}'}

    open_symbols = symbol_pair.keys()
    symbol_stack = Stack()

    for symbol in symbol_str:
        if symbol in open_symbols:
            symbol_stack.push(symbol)
        else:  # Is a closing symbol
            if symbol_stack.is_empty():  # if there is no Open symbol in the Stack, the string is unbalanced
                return False
            else:
                top_symbol = symbol_stack.pop()

                if symbol != symbol_pair[top_symbol]:
                    # If the Symbol in the top is not the open symbol of the same symbol we have a unbalanced string
                    return False

    if symbol_stack.is_empty():
        # if at the end of all the stack is empty, the string was balanced
        return True

    return False
