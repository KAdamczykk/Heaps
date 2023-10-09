""" Binary Heap structure by Krzysztof Adamczyk """
import math
import random
import networkx as nx
import matplotlib.pyplot as plt
class BinaryHeap:
    """
    Methods:
    * __init__()
    * push(number)
    * pop()
    * isEmpty()
    * printHeap()
    * clear()
    * search(value, index = 0)
    * remove(index)

    """
    def __init__(self):
        """
        Constructor make empty list, in which we can storage data and count, which saves length of list

        """
        self.list = []
        self.count = 0
    def push(self, number):
        """
        Method add value to proper place in heap

        """
        self.list.append(number)
        self.count +=1 
        k = self.count - 1
        while k != 0:
            parent_index = math.floor((k - 1)/2)
            parent_value = self.list[parent_index]
            if parent_value >= self.list[k]:
                break
            else:
                value = self.list[k]
                self.list[parent_index] = value
                self.list[k] = parent_value
                k = parent_index
        
    def pop(self):
        """
        Method remove first value in heap

        """
        if self.isEmpty == True:
            return
        else:
            self.list.pop(0)
            self.count -= 1
            last = self.list[self.count - 1]
            self.list.insert(0, last)
            self.list.pop(self.count -1)
            k = 0
            while k <= self.count -1:
                left_son_index = 2*k+1
                l  = False
                r = False
                if left_son_index < self.count:
                    left_son_value = self.list[left_son_index]
                    l = True
                right_son_index = 2*k+2
                if right_son_index < self.count:
                    right_son_value = self.list[right_son_index]
                    r = True
                parent_value = self.list[k]
                if parent_value >= max(left_son_value,right_son_value):
                    break
                else:
                    if left_son_value >= right_son_value and l == True:
                        self.list[k] = left_son_value
                        self.list[left_son_index] = parent_value
                        k = left_son_index
                    elif left_son_value < right_son_value and r == True:
                        self.list[k] = right_son_value
                        self.list[right_son_index] = parent_value
                        k = right_son_index
                    else:
                        break
    
    def isEmpty(self):
        """
        Method returns information, that heap is empty or not

        """
        if self.count == 0:
            return True
        else:
            return False
    def printHeap(self):
        """
        Method makes graphical representation of heap as graph

        """
        G = nx.Graph()
        highlighted_value = self.list[0]
        for i in range (0, self.count - 1):
            G.add_node(self.list[i])
            if 2 * i +1 < self.count:
                G.add_edge(self.list[i], self.list[2 * i +1])
            if 2 * i +2 < self.count:
                G.add_edge(self.list[i], self.list[2 * i +2])
        node_colors = ['red' if val == highlighted_value else 'skyblue' for val in G.nodes]
        pos = nx.spring_layout(G, seed=42)  
        nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, font_size=12, font_color='black', font_weight='bold')
        plt.show()
    def clear(self):
        """
        Method makes heap empty

        """
        self.list.clear
        self.count = 0
    def search(self, value, index = 0):
        """
        Method searches is the value that user input in Heap. Output: (True, index) or (False, None)

        """
        if index >= self.count:
            return False, None 

        if self.list[index] == value:
            return True, index

        if self.list[index] > value:
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            left_result = self.search(value, left_index)
            right_result = self.search(value, right_index)

            if left_result is (False, None):
                return right_result
            else:
                return left_result
        return False, None
    def remove(self, index):
        """
        Method remove value on index in Heap

        """
        assert index < self.count
        self.list[index] = self.list[self.count-1]
        self.count -=1
        self.list.pop(self.count - 1)
        k = index
        while k <= self.count -1:
            left_son_value = -math.inf
            right_son_value = -math.inf
            left_son_index = 2*k+1
            l  = False
            r = False
            if left_son_index < self.count:
                left_son_value = self.list[left_son_index]
                l = True
            right_son_index = 2*k+2
            if right_son_index < self.count:
                right_son_value = self.list[right_son_index]
                r = True
            parent_value = self.list[k]
            if parent_value >= max(left_son_value,right_son_value):
                break
            else:
                if left_son_value >= right_son_value and l == True:
                    self.list[k] = left_son_value
                    self.list[left_son_index] = parent_value
                    k = left_son_index
                elif left_son_value < right_son_value and r == True:
                    self.list[k] = right_son_value
                    self.list[right_son_index] = parent_value
                    k = right_son_index
                else:
                    break
       

def main():
    heap = BinaryHeap()
    for i in range(0,12):
        heap.push(random.randint(0, 99))
    heap.pop()
    heap.push(22)
    print(heap.list)
    print(heap.search(22))
    print(heap.search(4))
    heap.remove(5)
    print(heap.list)
    heap.printHeap()
if __name__ == "__main__":
    main()

