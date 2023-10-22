""" Binomial Heap structure by Krzysztof Adamczyk """
"""
Project:
classes and methods:
- node:
* __init__(value)
- BinominalHeap:
* __init__()
* insert(value)
* deleteMax()
* MergeTree(p1,p2) - static
* Extract(node_in) - static
* AddTree(node_, tree) - static
* UnionR(p1,p2) - static
* print_heap()
* _print_tree_structure(node, depth)

"""

class node:
    """
    Generic node, which contains value, rank(height of tree), next (sibling), prev(self or previous sibling), 
    child(reference to first added children)

    """
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.next = None
        self.prev = None
        self.child = None
class BinomialHeap:
    def __init__(self):
        """
        Constructor makes empty heap.

        """
        self.head = None
    def insert(self, value):
        """
        Method add new node with value (int or float) to Heap, with usuinf UnionR method

        """
        new_node = node(value)
        new_node.prev = None
        self.head = BinomialHeap.UnionR(new_node, self.head) 
    def deleteMax(self):
        """
        Method delete maximum value on roots line with using UnionR method. Output: node with maximum value or None

        """
        if self.head == None: # returning None if heap is empty 
            return None
        p = self.head # iterator
        pMax = None # max value node
        prev = None  # pMax previous node
        while p.next != None:
            if pMax is None or p.value > pMax.value:
                pMax = p 
                prevNode = prev
            prev = p
            p = p.next
        t = pMax.child # saving pMax child tree
        # deleting pMax node
        if prevNode.next.next != None: 
            prevNode.next.next.prev = prevNode
        else:
            self.head.prev = prevNode
        if prevNode.next != self.head:
            prevNode.next = prevNode.next.next
        else:
            self.head = self.head.next
        pMax.next = None
        pMax.prev = None
        self.head = BinomialHeap.UnionR(self.head,t) # UnionR method for self.head and pMax children
        return pMax
    @staticmethod
    def MergeTree(p1, p2):
        """
        Static method that merge p1 and p2 nodes and increase p1.rank
        Return: p1

        """
        if p1.value < p2.value:
            p1, p2 = p2, p1
        if p1.rank == 0:
            p1.child = p2
        else:
            p2.prev = p1.child.prev
            p2.prev.next = p2
            p1.child.prev = p2
        p1.rank += 1
        return p1
    @staticmethod
    def Extract(node_in):
        """
        Method extracts node that we want to delete from heap. Return: deleted node, rest of heap

        """
        p = node_in  
        node_in = node_in.next  

        if node_in is not None:
            node_in.prev = p.prev
        p.next = None
        p.prev = p
        return p, node_in
    @staticmethod
    def AddTree(node_, tree):
        """
        Method adds tree behind the node

        """
        if node_ == None:
            node_ = tree
        else:
            node_.prev.next = tree
            tree.prev = node_.prev
            node_.prev = tree
     
    @staticmethod
    def UnionR(p1,p2):
        """
        Method makes recursively the structure of Binominal Heap
        Input:  node1, node2
        Return: last_node

        """
        # if p1 or p2 is None we return other value
        if p1 == None: 
            return p2
        if p2 == None:
            return p1
        # if p1.rank < p2.rank, we use Extract method on p1 and UnionR method on p1 and p2 after that
        if p1.rank < p2.rank:
            t1, p1 = BinomialHeap.Extract(p1)
            p3 = BinomialHeap.UnionR(p1,p2)
            t1.prev = p3.prev
            t1.next = p3
            p3.prev = t1
            return t1 
        if p1.rank > p2.rank: # if p1.rank > p2.rank, we use UnionR(p2,p1)
            return BinomialHeap.UnionR(p2,p1)
        # if p1.rank == p2.rank we use two times extract function on p1 and p2, then we merge t1 and t2 trees, and UnionR on p1 and p2; and UnionR on p3 and t3
        t1, p1 = BinomialHeap.Extract(p1)
        t2, p2 = BinomialHeap.Extract(p2)
        t3 = BinomialHeap.MergeTree(t1,t2)
        p3 = BinomialHeap.UnionR(p1,p2)
        return BinomialHeap.UnionR(p3,t3)

    def print_heap(self):
        """
        Method prints Heap on console, if Heap is Empty it print: Empty Heap

        """
        if self.head is None:
            print("Empty Heap")
        else:
            print("Structure: ")
            self._print_tree_structure(self.head, 0)

    def _print_tree_structure(self, node, depth):
        """
        Method prints structure with conditions:
        * Every sibling has the same depth
        * prints rank of node behind value

        """
        if node is not None:
            print("  " * depth, end="")
            print(f"Rank {node.rank}: {node.value}")
            if node.child is not None:
                self._print_tree_structure(node.child, depth + 1)
            if node.next is not None:
                self._print_tree_structure(node.next, depth)

# T - E - S - T
def main():
    list1 = [1,4,7,8,9,2,3,11,12,10,55,76,60,-5]
    list2 = [40,15,-4,-2,69,33,22,5,6]
    heap1 = BinomialHeap()
    heap2 = BinomialHeap()
    for element1 in list1:
        heap1.insert(element1)
    for element2 in list2:
        heap2.insert(element2)
    heap1.print_heap()
    heap2.print_heap()
    print(heap1.deleteMax().value)
    heap1.print_heap()
    t1 = BinomialHeap()
    t1.head = BinomialHeap.UnionR(heap1.head, heap2.head)
    t1.print_heap()
if __name__ == '__main__':
    main()