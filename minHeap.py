# created by Avi Fenesh
# i took most of the structure of the minHeap from gfg and edited it for my own need
# the changes are that here i store the log files objects in the min_heap and compare the time stamp instead of regular
# instance
# another change is i check when try to return the min if this is the last line in the file, if it is i return min
# like usual, else i get the line, then get the next one from the file and use heapify

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = 0
        self.FRONT = 0

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return (2 * pos) + 1

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 2

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):

            if (self.Heap[pos].get_time_stamp() > self.Heap[self.leftChild(pos)].get_time_stamp() or
                    self.Heap[pos].get_time_stamp() > self.Heap[self.rightChild(pos)].get_time_stamp()):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)].get_time_stamp() < self.Heap[self.rightChild(pos)].get_time_stamp():
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size == 0:  # if its the first element
            self.Heap[0] = element
            self.size += 1
            return
        else:
            if self.size >= self.maxsize:
                return
            self.Heap[self.size] = element
            self.size += 1

            current = self.size - 1

            # heapify the new element to his place
            while self.Heap[current].get_time_stamp() < self.Heap[self.parent(current)].get_time_stamp():
                self.swap(current, self.parent(current))
                current = self.parent(current)

    # Function to remove and return the minimum
    # element from the heap
    # if its the last line in the file do it as usual,
    # else get the line and then heapify with the new line timeStamp value
    def remove(self):
        popped, last_check = self.Heap[self.FRONT].get_line()

        if last_check == 0:  # get_line return 0 if last line, then we min_heapify normally
            self.Heap[self.FRONT] = self.Heap[self.size - 1]
            self.size -= 1
            if self.size == 0:
                return popped
            self.minHeapify(self.FRONT)
            return popped

        else:  # if not the last line, get the line and heapify withe the time stamp of the next line
            self.minHeapify(self.FRONT)
            return popped