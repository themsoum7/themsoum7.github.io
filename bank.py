"""
File: linkedqueue.py
Author: Ken Lambert
"""

from node import Node
from abstractcollection import AbstractCollection
import random

class LinkedQueue(AbstractCollection):
    """A link-based queue implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        pass

    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front.data

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass

    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node(item, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

class Cachier(LinkedQueue):
    '''
    Adding and serving customers of the bank by cashier.
    '''
    def __init__(self):
        self._customersServed = 0
        self._totalCustomerWaitTime = 0
        self._queue = LinkedQueue()
        self.currentCustomer = None

    def addCustomer(self, c):
        '''
        Adding customer.
        '''
        self._queue(c)

    def serveCustomer(self, currentTime):
        '''
        Serving customer.
        '''
        if self._currentCustomer is None:
            print("There was no customers yet")
            if self._queue.isEmpty():
                return None
            else:
                self._currentCustomer = self._queue()
                self._totalCustomerWaitTime +=  currentTime
                self._totalCustomer.arrivalTime()
                self._customersServed += 1
        self._currentCustomer.serve()
        if self._currentCustomer.amountOfServiceNeeded() == 0:
            self._currentCustomer = None

    def __str__(self):
        '''
        Outputing information about queue.
        '''
        result = "Total for the cashier\n" + "Number of customers served: " + str(self._customersServed) + "\n"
        if self._customersServed != 0:
            aveWaitTime = self._totalCustomerWaitTime / self._customersServed
            result +=  "Number of customers left the queue: " + str(len(self._queue)) + "\n" + "waiting to be served: " + "%5.2f" %aveWaitTime
        return result

class Customer():
    '''
    Contains modules that are adding new customers to the queue(coming customer) and modules that are attached to customer functions.
    '''
    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival, arrivalTime, averageTimePerCustomer):
        '''
        New customer coming.
        '''
        if random.random() <= probabilityOfNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None

    def __init__(self, arrivalTime, serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountOfServiceNeeded = serviceNeeded

    def arrivalTime(self):
        '''
        Return of arrival time of customer.
        '''
        return self._arrivalTime

    def amountOfServiceNeeded(self):
        '''
        Return of amount of customers that need cashier service.
        '''
        return self._amountOfServiceNeeded

    def serve(self):
        '''
        Accepts a unit of service from the cashier.
        '''
        self._amountOfServiceNeeded -= 1
