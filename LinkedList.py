class Node:
    """
    Methods:
    --------------
    * __init__
    
    """
    def __init__(self, val, next):
        """
        Creating nodes for store values and references
        Parameters
        ----------
        val : integer value.
        next : reference to next node.

        """
        self.val = val
        self.next = next
    
class LinkedList:  
    """
    Methods:
    --------------
    * __init__
    * pushFront
    * pushLast
    * insertAfter
    * delFront
    * delLast
    * remove
    * findMax
    * findMin
    * get
    * search
    * getHead
    * getTail
    * delMax
    * delMin
    * clear
    * size
    * isEmpty
    * printAll
    * toList
    * fromList
    * reverse
    * update
    """
    def __init__(self):  
        """
        Creating empty list with head (first element), tail (last element) 
        and size (to optimize code; default zero)
        
        """
        self.head = None
        self.tail = None
        self.sized = 0
    def pushFront(self, v):
        """
        Inserting new value on the left (front) of the list

        Parameters
        ----------
        v : value, that we want to make first.

        """
        temp = Node(v,None)
        temp.next = self.head
        self.head = temp
        if not self.tail:
            self.tail = temp
        self.sized +=1
    def pushLast(self, v):
        """
        Inserting value on the right(last) place in the list

        Parameters
        ----------
        v : value to insert.

        """
        temp = Node(v,None)
        if not self.head:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp     
        self.sized += 1
    def insertAfter(self, after, value):
        """
        Method inserts value after existing element

        Parameters
        ----------
        after : after which value we want to insert.
        value : inserting value

        """
        temp = self.head
        while temp.val != after:
            temp = temp.next
        newNode = Node(value, temp.next)
        temp.next = newNode
        self.sized += 1
    def delFront(self):
        """
        Deleting first value on the list

        """
        if not self.head == None:
            self.head = self.head.next
        self.sized -= 1
    def delLast(self):
        """
        Deleting last value on the list

        """
        P = self.head
        while P.next.next != None:
            P = P.next
        self.tail = P
        P.next = None
        self.sized -= 1
    def remove(self, val):
        """
        Method removes first appearance of value

        Parameters
        ----------
        val : value to remove.

        """
        temp = self.head
        while temp.next.val != val or temp == None:
            temp = temp.next
        temp.next = temp.next.next
        self.sized -= 1
    def findMax(self):
        """
        Finding maximum value on the list

        Returns
        -------
        val : max value.

        """
        temp = self.head
        val = self.head.val
        while temp != None:
            if temp.val > val:
                val = temp.val
            temp = temp.next
        return val
    def findMin(self):
        """
        Finding minimun value on the list

        Returns
        -------
        val : min value.

        """
        temp = self.head
        val = self.head.val
        while temp != None:
            if temp.val < val:
                val = temp.val
            temp = temp.next
        return val
    def get(self, index):
        """
        Method returns value that is placed on index. First index is 0.

        Parameters
        ----------
        index : position on list that user want to get value.

        Returns
        -------
        Value on index.

        """
        temp = self.head
        for i in range(0,index):
            temp = temp.next
        return temp.val
    def search(self, value):
        """
        Method returns the information that value user inputs is on the list

        Parameters
        ----------
        value : int - what we want to search.

        Returns
        -------
        bool
           True if list include value, false if not.

        """
        temp = self.head
        while temp != None:
            if temp.val == value:
                return True
            temp = temp.next
        return False
    def getHead(self):
        """
        Method returns value on the head of list

        """
        return self.head.val
    def getTail(self):
        """
        Method returns value on the tail of list

        """
        return self.tail.val
    def delMax(self):
        """
        Deleting maximum value on the list, including findMax method

        """
        P = self.head
        while P.next.val != self.findMax():
            P = P.next
        P.next = P.next.next
        self.sized -= 1
    def delMin(self):
        """
        Deleting minimum value on the list, including findMin method

        """
        P = self.head
        while P.next.val != self.findMin():
            P = P.next
        P.next = P.next.next
        self.sized -= 1
    def clear(self):
        """
        Removing all values from the list.

        """
        self.head = None
        self.sized = 0
    def size(self):
        """
        Method return size of the list

        Returns
        -------
        int
            size.

        """
        return self.sized
    def isEmpty(self):
        """
        Method returns information that the list is empty or no
        
        """
        if self.head == None:
            return True
        else:
            return False
    def printAll(self):
        """
        Printing List as output

        """
        temp = self.head
        while temp != None:
            print(temp.val, end = " ")
            temp = temp.next
    def toList(self):
        """
        Method convert LinkedList to default Python list

        """
        List = []
        temp = self.head
        while temp != None:
            List.append(temp.val)
            temp = temp.next
        return List
    def fromList(self, List):
        """
        Method convert default Python list to LinkedList by using pushFront Method

        """
        n = len(List) - 1
        for i in range (n,-1,-1):
            val = List[i]
            self.pushFront(val)
    def reverse(self):
        """
        Method swaps values on the list in reverse order, using update method

        """
        temp = self.head
        tm = LinkedList()
        while temp != None:
            val = temp.val
            tm.pushFront(val)
            temp = temp.next
        self.clear()
        self.update(tm)
    def update(self, other):
        """
        Method updates self attributes by other LinkedList attributes (head,tail)
        
        """
        self.head = other.head
        self.tail = other.tail
        
'''      
# T E S T 
otlist = LinkedList()
for i in range (0,15):
    otlist.pushFront(i)
otlist.pushLast(-9)
otlist.delFront()
otlist.delLast()
otlist.delLast()
otlist.pushFront(4)
otlist.pushFront(4)
otlist.pushFront(7)
otlist.pushFront(3)
otlist.pushFront(5)
otlist.pushFront(2)
otlist.delMax()
otlist.delMin()
print(otlist.size())
otlist.insertAfter(4, 15)
otlist.remove(7)
print(otlist.get(0))
print(otlist.search(-8))
listt = otlist.toList()
print(otlist.toList())
ot = LinkedList()
ot.fromList(listt)
otlist.reverse()
otlist.printAll()
print()
ot.printAll()
'''


