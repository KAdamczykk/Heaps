""" LeftistHeap structure by Krzysztof Adamczyk """
"""
Project:
classes and methods:
*node:
-__init__(value, left, right, dist)
*LeftistHeap:
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
    Generic node, with references to left and right sons. Every node contains also inforamtion about npl (dist; null path length)
    and value on added node.
    Default: left = None, right = None, dist = -1

    """
    def __init__(self, value, left = None, right = None, dist = -1):
        self.value = value
        self.left = left
        self.right = right
        self.dist = dist
class LeftistHeap:
    def __init__(self):
        """
        Constructor creates empty Leftist Heap with root = None. Root is the maximum value in Heap

        """
        self.root = None
    @staticmethod
    def Union(p1 = None, p2 = None):
        """
        Union is method, which makes right Leftist Heap: it has Heap structure and left subtree has larger values then right subtree.
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
        # 3) recursively we makes right Leftist on right subtree
        p1.right = LeftistHeap.Union(p1.right, p2)
        # 4) if right subtree has larger values, we swap it with left subtree
        if (p1.left == None and p1.right is not None) or (p1.left is not None and p1.left.value < p1.right.value):
            p1.left, p1.right = p1.right, p1.left
        # 5) updating dist (npl) option
        if p1.right:
            p1.dist = p1.right.dist + 1 
        else:
            p1.dist = 0
        return p1
    def findMax(self):
        """ 
        Method return maximum value of Leftist Heap (root)

        """
        return self.root
    def insert(self, value):
        """
        Method insert new node with inputted value and uses Union method to input it in right place.
        This is merging of heap that we are operating with size of one heap.

        """
        new_node = node(value)
        self.root = LeftistHeap.Union(new_node, self.root)
    def delMax(self):
        """
        Method delete the maximum value on Leftist Heap and use Union method to repair the Leftist Heap structure.
        If Heap is empty it returns string: 'empty heap'.

        """
        if self.isEmpty():
            return 'empty heap'
        self.root = LeftistHeap.Union(self.root.left, self.root.right)
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
        Method prints Leftist Heap: node - node on which we want to start (usually root), indent- string of character to indent,
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
    heap1 = LeftistHeap()
    heap2 = LeftistHeap()
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
    heap1.root = LeftistHeap.Union(heap1.root, heap2.root)
    heap1.printTree(heap1.root)
if __name__ == "__main__":
    main()
    

        