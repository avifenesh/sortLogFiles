"""
created by Avi Fenesh
explanation:
i took most of the structure of the minHeap from gfg and edited it for my own need
the changes are that here i store the log files objects in the min_heap and compare the time stamp instead of regular
instance
another change is i check when try to return the min if this is the last line in the file, if it is i return min
like usual, else i get the line, then get the next one from the file and use heapify
"""

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.FRONT = 0

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def left_child(self, pos):
        return (2 * pos) + 1

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def right_child(self, pos):
        return (2 * pos) + 2

    # Function that returns true if the passed
    # node is a leaf node
    def is_leaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    # Function to heapify the node at pos
    def min_heapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.is_leaf(pos):

            if (self.heap[pos].time_stamp > self.heap[self.left_child(pos)].time_stamp or
                    self.heap[pos].time_stamp > self.heap[self.right_child(pos)].time_stamp):

                # Swap with the left child and heapify
                # the left child
                if self.heap[self.left_child(pos)].time_stamp < self.heap[self.right_child(pos)].time_stamp:
                    self.swap(pos, self.left_child(pos))
                    self.min_heapify(self.left_child(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.min_heapify(self.right_child(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size == 0:  # if its the first element
            self.heap[0] = element
            self.size += 1
            return
        else:
            if self.size >= self.maxsize:
                return
            self.heap[self.size] = element
            self.size += 1

            current = self.size - 1

            # heapify the new element to his place
            while self.heap[current].time_stamp < self.heap[self.parent(current)].time_stamp:
                self.swap(current, self.parent(current))
                current = self.parent(current)

    # Function to remove and return the minimum
    # element from the heap
    # if its the last line in the file do it as usual,
    # else get the line and then heapify with the new line timeStamp value
    def remove(self):
        popped, last_check = self.heap[self.FRONT].get_line()

        if last_check == 0:  # get_line return 0 if last line, then we min_heapify normally
            self.heap[self.FRONT] = self.heap[self.size - 1]
            self.size -= 1
            if self.size == 0:
                return popped
            self.min_heapify(self.FRONT)
            return popped

        else:  # if not the last line, get the line and heapify withe the time stamp of the next line
            self.min_heapify(self.FRONT)
            return popped