""" Fibonacci Heap structure by Krzysztof Adamczyk """
import math
class Node:
    """
    Generating nodes with: value, degree of node and pointers to previous, next, child and parent nodes.
    Principle of operation on pointers:
    * next point to next element on same degree on the same tree, last element is None
    * prev point to previous element on same degree on the same tree, root.prev is last element in the level
    * child point to subroot on every level, from there next and prev work the same as normal
    * parent point to parent, so all elements on the level had the same parent
    * degree - maximum path to the leaf

    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = self
        self.parent = None
        self.child = None
        self.degree = 0

class FibonacciHeap:
    """
    Methods:
    - __init__()
    - insert(value)
    - Union(p2)
    - returnMax()
    - isEmpty()
    - clear()
    - deleteMax()
    - Consolidate()
    - link(smaller, larger) - static
    - print_fibonacci_heap()
    - _print_node(node, level)
    """
    def __init__(self):
        """
        Creating empty heap, with root and max pointers. Also contains total number of nodes in Heap

        """
        self.max = None
        self.root = None
        self.num_nodes = 0
    def insert(self, value):
        """ 
        Inserting value as new Fibonacci Heap using Union mehtod

        """
        new_node = Node(value)
        f = FibonacciHeap()
        f.max = new_node
        f.root = new_node
        f.num_nodes = 1
        self.Union(f)
    def Union(self,p2): 
        """
        Union method merge two heaps to one structure in constant time

        """
        # if self or p2 heap is empty -> end the function
        if self.root is None:
            self.root = p2.root
            self.max = p2.max
            self.num_nodes = p2.num_nodes
            return 
        if p2 is None: 
            return 
        # 3 methods of merging self with p2, because we want to follow the rules of node's working
        # first option: self has more trees than one
        if self.root.prev != self.root:
            self.root.prev.next = p2.root
            var = self.root.prev
            self.root.prev = p2.root.prev
            p2.root.prev = var
        # self has one tree, but p2 has more than one tree. We must to point self.root.prev on the end of p2 and merge p2 to self
        elif self.root.prev == self.root and p2.root.prev != p2.root:
            self.root.prev = p2.root.prev
            self.root.next = p2.root
            p2.root.prev = self.root
        # self and p2 have only one tree: self.root.prev is p2.root, and p2.root.prev is p1.root
        else:
            self.root.next = p2.root
            self.root.prev = p2.root
            p2.root.prev = self.root
        # updating max
        if self.max.value < p2.max.value:
            self.max = p2.max
        # updating num_nodes
        self.num_nodes +=  p2.num_nodes
        
    def returnMax(self):
        """
        Returns max value without deleting

        """
        return self.max.value
    def isEmpty(self):
        """
        Returns information that heap is empty or no

        """
        if self.root is None:
            return True
        return False
    def clear(self):
        """
        Remove all values and nodes from heap

        """
        self.max = None
        self.root = None
        self.num_nodes = 0
    def deleteMax(self):
        """
        Deleting maximum value with consolidation of trees, returns max value too

        """
        if self.root == None:
            return
        delmax = self.max
        # if max node has child, we need to detach and place them on roots level as new trees
        if self.max.child != None:
            p = self.max.child
            while p.next != None:
                child = p
                self.max.prev.next = child
                child.prev = self.max.prev
                child.next = self.max
                self.max.prev = child
                p = p.next
        # removing max node
        self.max.prev.next = self.max.next
        self.max.next.prev = self.max.prev
        self.num_nodes -= 1

        # Consolidation of trees
        self.Consolidate()

        # updating max node 
        p = self.root
        max_node = self.root
        max_val = self.root.value
        while p.next != None:
            if p.value > max_val:
                max_val = p.value
                max_node = p
            p = p.next    
        self.max = max_node
        return delmax.value
    def Consolidate(self):
        """
        This method merge trees, that all of them must have different heights.

        """
        # calculation of maximum height of tree and creating array that index = height of tree
        max_height = int(math.log2(self.num_nodes))
        array = [None] * (max_height + 1)
        # putting all nodes on roots level into list
        current = self.root
        roots = []
        while current != None:
            roots.append(current)
            current = current.next
        # for every element in roots we want to do one of thwo things:
        # - if we have any element of the same degree in array, we merge the trees, and add to array on degree + 1 index etc.
        # - else we put this node into array
        for node in roots:
            degree = node.degree
            while array[degree] != None:
                other = array[degree]
                if node.value < other.value:
                    node, other = other, node
                node = FibonacciHeap.link(other, node)
                array[degree] = None
                degree += 1
            array[degree] = node
        # removing all None values from array
        array = [x for x in array if x is not None]
        # creating Fibonacci Heap from array
        self.root = array[0]
        self.root.prev = array[len(array) - 1]
        for i in range(0,len(array)):
            if i < len(array) - 1:
                array[i].next = array[i + 1]
            if i > 0:
                array[i].prev = array[i - 1]
        array[-1].next = None
        self.root = array[0]

    @staticmethod
    def link(smaller, larger):
        """
        Merging two nodes following the rules of Maximum Heap

        """
        # if there is no child, we add smaller as a child of larger
        if larger.child == None:
            larger.child = smaller
            smaller.parent = larger
            smaller.next = None
            smaller.prev = smaller
        # if there is child, but this is only one node on the level, we needs to tho the same thing with prev and next as we do in Union method
        elif larger.child != None and larger.child.next == None:
            larger.child.prev = smaller
            smaller.next = larger.child.next
            smaller.prev = larger.child
            larger.child.next = smaller
            smaller.parent = larger
        else:
            smaller.next = larger.child.next
            smaller.prev = larger.child
            larger.child.next = smaller
            smaller.parent = larger
        # degree increase
        larger.degree += 1
        return larger
    def print_fibonacci_heap(self):
        """
        Function prints the Fibonacci Heap with rules:
        - every node is represented: Value: val, Degree: deg
        - elements on the same lavel have the same indentation
        """
        if self.root is None:
            print("Empty Fibonacci Heap")
            return

        print("Fibonacci Heap:")
        # again we made a list of elements on root level
        current = self.root
        nodes = [current]
        while current.next != None:
            current = current.next
            nodes.append(current)
        # we are using _print_node method for every element in nodes
        for node in nodes:
            self._print_node(node, 0)

    def _print_node(self, node, level):
        """
        Recursively printing all elements in the same tree.

        """
        indent = "  " * level
        print(f"{indent}Value: {node.value}, Degree: {node.degree}")
        # printing all elements on the same level with the same indentation. We do this, as long as we have the elements that have child
        if node.child:
            child = node.child
            while True:
                self._print_node(child, level + 1)
                if child.next == None:
                    break
                child = child.next

# T - E - S - T
def main():
    fib = FibonacciHeap()
    fib.insert(7)
    fib.insert(11)
    fib.insert(12)
    fib.insert(1)
    fib.insert(5)
    fib.insert(4)
    fib.print_fibonacci_heap()
    print(fib.returnMax())
    print(fib.isEmpty())
    print(fib.deleteMax())
    fib.print_fibonacci_heap()

if __name__ == '__main__':
    main()

