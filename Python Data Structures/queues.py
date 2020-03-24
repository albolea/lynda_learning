########################################################################
#### Course: Python Data Structures: Stacks, Queues, and Deques     ####
#########################################################################

class Queue():
    """
    FIFO
    We are using a List as the base of our Queue. The left Side of the List is the end (back) of our Queue and the right
    side is the beginning (front) of the Queue.
    """

    def __init__(self):
        """Constructor for Queue"""
        self.items = []

    def enqueue(self, item):
        """
        This method adds an Item to the queue
        The runtime for this method is O(n) - linear- because will end up shifting all indexes from the list to the
        right, which is a O(n) runtime.
        :return: None
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        This method removes and return the
        right, which is a O(n) runtime.
        :return: Item
        The runtime for this method is O(1)
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """
        Returns (without Remove) the First item from the list that is the front of our Queue.
        The runtime for this method is O(1).
        """
        if self.items:
            return self.items[-1]

        return None

    def size(self):
        """
        Returns the size of the Queue.
        The runtime for this method is O(1).
        """
        return len(self.items)

    def is_empty(self):
        """
        :return True if the Queue is empty and False if not
        The runtime for this method is O(1).
        """
        return self.items == []


class PrintQueue(Queue):
    def __init__(self):
        super().__init__()


class Job:
    """"""

    def __init__(self):
        """Constructor for Job"""
        from random import randint
        self.pages = randint(1, 10)

    def printPage(self):
        if self.pages:
            self.pages -= 1

    def checkComplete(self):
        if self.pages == 0:
            return True

        return False


class Printer:
    """"""

    def __init__(self):
        """Constructor for Printer"""
        self.current_job = None
        self.current_queue = None

    def get_queue(self, print_queue):
        self.current_queue = print_queue

    def get_job(self, print_queue):
        try:
            self.current_job = self.current_queue.dequeue()
        except IndexError: # Queue is Empty
            return "No more jobs to print"

    def print_job(self):
        job = self.current_job
        while not job.checkComplete():
            job.printPage()
        if job.checkComplete():
            print("Job was printed")
        else:
            print("An error occurred during the last job")

    def print_jobs(self):
        while not self.current_queue.is_empty():
            self.current_job = self.current_queue.dequeue()
            self.print_job()

        return "All jobs were executed"


my_printer = Printer()
print_q = PrintQueue()
print_q.enqueue(Job())
print_q.enqueue(Job())
my_printer.get_queue(print_q)
print(my_printer.print_jobs())
