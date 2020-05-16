import heapq

class myHeapThingy:
    def __init__(self):
        self.h = []
        heapq.heapify(self.h)

def addItem(h, intVal):
    heapq.heappush(h, int(intVal))


def customPopulate(h):
    heapq.heappush(h, 1)
    heapq.heappush(h, 3)
    heapq.heappush(h, 2)
    heapq.heappush(h, 0)
    heapq.heappush(h, 5)
    heapq.heappush(h, 1)
    heapq.heappush(h, 4)
    heapq.heappush(h, 3)

def makeHeap(h):
    h.sort()

def populateHeapSequence(h, numItems, isReversed):
    if not reversed:
        for i in range(numItems):
            heapq.heappush(h, i)
    else:
        for i in reversed(range(numItems)):
            heapq.heappush(h, i)
    #heapq.heapify(h)


def checkValues(h):
    print("for each k, h[2 * k + 1] and h[2 * k + 2] are the children\n")
    for k in range(len(h)):
        print("Item {} ".format(k))
        if 2 * k + 2 < len(h):
            print("Value: {}".format(h[k]))
            print("Right child: {} \nFollows heap rule: {}".format(int(h[2 * k + 2]), int(h[k]) <= int(h[2 * k + 2] )))
            print("LEFT child: {} \nFollows heap rule: {}\n".format(int(h[2 * k + 1]), int(h[k]) <= int(h[2 * k + 1] )))
        elif 2 * k + 1 < len(h):
            print("Value: {}".format(h[k]))
            print("LEFT child: {} \nFollows heap rule: {}\n".format(int(h[2 * k + 1]), int(h[k]) <= int(h[2 * k + 1])))
        else:
            print("Value: {}".format(h[k]))
            print("No children\n")

def printHeap(h):
    print(h, "\n")