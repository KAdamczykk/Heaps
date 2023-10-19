""" Skew Heap structure by Krzysztof Adamczyk """
"""
Project:
classes and methods:
*node:
-__init__(value, left, right, dist)
*Skew Heap:
-__init__()
-Union(p1,p2) - static
-findMax()
-insert(value)
-delMax()
-isEmpty()
-clear()
-print_tree(node, index, prefix)

"""
class node:
    """
    Generic node, with references to left and right sons and value on added node.
    Default: left = None, right = None

    """
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class SkewHeap:
    def __init__(self):
        """
        Constructor creates empty Skew Heap with root = None. Root is the maximum value in Heap

        """
        self.root = None
    @staticmethod
    def Union(p1 = None, p2 = None):
        """
        Union method merge twp heap by with the algorithm, which is written in comments
        Input: two heaps
        Output: one heap which contains p1 and p2 values.

        """
        # 1) check that p1 or p2 is empty
        if not p1:
            return p2
        elif not p2:
            return p1
        # 2) we want to operate on p1 as root, so if p2 has larger value than p1, we swap them
        if p1.value < p2.value:
            p2, p1= p1, p2
        # 3) swapping p1.left with p1.right, so new p1.right is final subtree
        p1.left, p1.right = p1.right, p1.left
        # 4) we merge recursively p1.left with p2, so we will keep Heap structure 
        p1.left = SkewHeap.Union(p2, p1.left)
        # 5) returning p1
        return p1
    def findMax(self):
        """ 
        Method return maximum value of Skew Heap (root)

        """
        return self.root
    def insert(self, value):
        """
        Method insert new node with inputted value and uses Union method to input it in right place.
        This is merging of heap that we are operating with size of one heap.

        """
        new_node = node(value)
        self.root = SkewHeap.Union(new_node, self.root)
    def delMax(self):
        """
        Method delete the maximum value on Skew Heap and use Union method to repair the Skew Heap structure.
        If Heap is empty it returns string: 'empty heap'.

        """
        if self.isEmpty():
            return 'empty heap'
        self.root = SkewHeap.Union(self.root.left, self.root.right)
    def isEmpty(self):
        """ 
        Method returns information, that Heap is empty or not. (boolean)

        """
        if self.root == None:
            return True
        else:
            return False
    def clear(self):
        """
        Removing all values from Heap

        """
        self.root = None
    def printTree(self, node, indent="", prefix=""):
        """
        Method prints Skew Heap: node - node on which we want to start (usually root), indent- string of character to indent,
        prefix- symbol(L---, R---) that informs, that node is left or right son.

        """
        if node is not None:
            print(indent + prefix + str(node.value))
            indent += "  "
            self.printTree(node.left, indent, "L---")
            self.printTree(node.right, indent, "R---")
# T - E - S - T
def main():
    list1 = [6,2,8,3,11,22,75,32,0,1,9,4]
    list2 = [-1,5,12,14,15,-5]
    heap1 = SkewHeap()
    heap2 = SkewHeap()
    for i in range(0,len(list1)):
        heap1.insert(list1[i])
    for j in range(0,len(list2)):
        heap2.insert(list2[j])
    heap1.printTree(heap1.root)
    heap2.printTree(heap2.root)
    heap1.delMax()
    heap1.printTree(heap1.root)
    print(heap2.isEmpty())
    print(heap2.findMax())
    heap1.root = SkewHeap.Union(heap1.root, heap2.root)
    heap1.printTree(heap1.root)
if __name__ == "__main__":
    main()
    

        