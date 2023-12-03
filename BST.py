""" BST structure by Krzysztof Adamczyk """
"""
BST structure with insert(value), search(value) and delete(value) and visualize methods
Node: left - child, right- child, value- integer value

"""
# libraries for visualisation and random for randomize choice of tree in deleting
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import random
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, value0): # creating BST with root 
        self.root = Node(value0)
    def insert(self, value): # inserting value
        inserted_node = Node(value)
        p, last = self.search(value)
        if(p != None): # if the value is in bst, we skipped insert function
            return
        if(last.value > value):
            last.left = inserted_node
        else:
            last.right = inserted_node
        
    def search(self,value): # searching for value in BST
        p = self.root
        last = p
        while(True):
            if(p == None):
                break
            if(value == p.value):
                break
            if(value < p.value):
                last = p
                p = p.left
            else:
                last = p
                p = p.right
        return p, last
    def delete(self,value): # deleting value from bst
        p, last = self.search(value)
        if p is None: # if the value isn't in bst, return
            return
        if p.left is None and p.right is None: # p is leaf
            if(p.value < last.value):
                last.left = None
            else:
                last.right = None
            return
        if p.left is None or p.right is None: # p has only one child
            if p.value < last.value and p.left is None:
                last.left = p.right
            if p.value < last.value and p.right is None:
                last.left = p.left
            if p.value > last.value and p.left is None:
                last.right = p.right
            if p.value > last.value and p.right is None:
                last.right = p.left
        else: # p has 2 children
            probability = random.randint(0,1) # randomizer for choice of subtree
            temp = None
            tmp = p
            if probability == 0:
                tmp = tmp.left
                while True:
                    if tmp.right is None:
                        temp = tmp
                        p.left = None
                        break
                    if tmp.right.right == None:
                        temp = tmp.right
                        break
                    tmp = tmp.right
                tmp.right = temp.left
                temp.left = p.left
                temp.right = p.right
                if last.value > p.value:
                    last.left = temp
                else:
                    last.right = temp
            else:
                tmp = tmp.right
                while True:
                    if tmp.left is None:
                        temp = tmp
                        p.right = None
                        break
                    if tmp.left.left == None:
                        temp = tmp.left
                        break
                    tmp = tmp.left
                tmp.left = temp.right
                temp.right = p.right
                temp.left = p.left
                if last.value > p.value:
                    last.left = temp
                else:
                    last.right = temp
                    
    # BST visualization 
    def inorder_traversal(self, node, x, y, dx, level):
        if node:
            if node.left:
                plt.plot([x, x - dx / 2], [y - 1, y - 2], color='black')
            if node.right:
                plt.plot([x, x + dx / 2], [y - 1, y - 2], color='black')
            plt.text(x, y, str(node.value), ha='center', va='center',
                     bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
            self.inorder_traversal(node.left, x - dx / 2, y - 2, dx / 2, level + 1)
            self.inorder_traversal(node.right, x + dx / 2, y - 2, dx / 2, level + 1)

    def visualize_bst(self):
        plt.figure(figsize=(12, 8))
        self.inorder_traversal(self.root, 0, 0, 12, 0)
        plt.axis('off')
        plt.show()
# T - E - S - T
def main():
    bst = BST(10)
    p, l = bst.search(10)
    print(p)
    p, l = bst.search(5)
    print(p)
    bst.insert(2)
    bst.insert(8)
    bst.insert(0)
    bst.insert(12)
    bst.insert(18)
    bst.insert(20)
    bst.insert(4)
    bst.insert(6)
    bst.insert(15)
    bst.insert(23)
    #bst.visualize_bst()
    bst.delete(23)
    bst.delete(222)
    bst.delete(4)
    bst.delete(2)
    bst.delete(18)
    bst.visualize_bst()
if __name__ == '__main__':
    main()