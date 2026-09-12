 

class Heap:
    def __init__(self,size):
        self.heap = (size+1) *[None]
        self.heapSize = 0
        self.maxSize = size+1

def peek(rootnode):
    if not rootnode:
        return 
    else:
        return rootnode.heap[1]

def sizeOfheap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapSize

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(rootNode.heapSize +1):
            print(rootNode.heap[i])

def heapifyTreeInsert(rootNode , index , heapType):
    parent_idx = int(index/2)
    if index <= 1:
        return
    if heapType == 'Min':
        if rootNode.heap[index] < rootNode.heap[parent_idx]:
            temp = rootNode.heap[index]
            rootNode.heap[index] = rootNode.heap[parent_idx]
            rootNode.heap[parent_idx] = temp
        heapifyTreeInsert(rootNode , parent_idx , heapType)
    
    elif heapType == 'Max':
        if rootNode.heap[index] > rootNode.heap[parent_idx]:
            temp = rootNode.heap[index]
            rootNode.heap[index] = rootNode.heap[parent_idx]
            rootNode.heap[parent_idx] = temp
        heapifyTreeInsert(rootNode , parent_idx,heapType)

def insertNode(rootNode , nodevalue , heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.heap[rootNode.heapSize+1] = nodevalue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode , rootNode.heapSize , heapType)
    print("The value has been inserted successfully")


def heapifyTreeExtract(rootNode , index , heaptype):
    leftIndex = index *2
    rightIndex = index*2+1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heaptype == 'Min':
            if rootNode.heap[index] > rootNode.heap[leftIndex]:
                temp = rootNode.heap[index]
                rootNode.heap[index] = rootNode.heap[leftIndex]
                rootNode.heap[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heaptype == 'Min':
            if rootNode.heap[leftIndex] < rootNode.heap[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.heap[index] > rootNode.heap[swapChild]:
                temp = rootNode.heap[index]
                rootNode.heap[index] = rootNode.heap[swapChild]
                rootNode.heap[swapChild] = temp
        else:
            if rootNode.heap[leftIndex] > rootNode.heap[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            
            if rootNode.heap[index] < rootNode.heap[swapChild]:
                temp = rootNode.heap[index]
                rootNode.heap[index] = rootNode.heap[swapChild]
                rootNode.heap[swapChild] = temp
    heapifyTreeExtract(rootNode,swapChild,heaptype)

def extractNode(rootNode , heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode=rootNode.heap[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode

def deleteEntireBP(rootNode):
    rootNode.customList = None

newHeap = Heap(5)
insertNode(newHeap, 4, "Max")
insertNode(newHeap, 5, "Max")
insertNode(newHeap, 2, "Max")
insertNode(newHeap, 1, "Max")
levelOrder(newHeap)
