""" Biparental Heap (Beap) structure by Krzysztof Adamczyk """
import math

class BiparentalHeap:
    """
    Methods:
    * __init__()
    * add_new_value(value)
    * UpBeap(index)
    * pop()
    * DownBeap(index)
    * search(value)
    * isEmpty()
    * clear()
    * remove(value)
    
    """
    def __init__(self):
        """
        Constructor makes empty list and count, wich storage information about lenght of the list

        """
        self.list = []
        self.count = 0
    def add_new_value(self, value):
        """
        Adding new value to Beap and updating Beap by UpBeap method

        """
        self.list.append(value)
        self.count+=1
        if self.count > 1:
            self.UpBeap(index = self.count - 1)
    def UpBeap(self, index):
        """
        Method update list after adding new values to Beap structure

        """
        while index > 0:
            i = int(math.ceil(0.5*(-1+math.sqrt(1.0+8*index))))
            parent_index_one = index - i 
            parent_index_two = index - i + 1
            if parent_index_one < 0:
                parent_index_one = parent_index_two
            if parent_index_two < 0:
                parent_index_two = parent_index_one
            if self.list[parent_index_one] < self.list[index] or self.list[parent_index_two] < self.list[index]:
                if self.list[parent_index_one] >= self.list[parent_index_two]:
                    self.list[parent_index_two], self.list[index] = self.list[index], self.list[parent_index_two]
                    index = parent_index_two
                else:
                    self.list[parent_index_one], self.list[index] = self.list[index], self.list[parent_index_one]
                    index = parent_index_one
            else:
                break
    def pop(self):
        """
        Deleting maximum value in Beap and updating Beap by DownBeap method

        """
        self.list.pop(0)
        self.count -= 1
        self.list.insert(0, self.list[self.count - 1])
        self.list.pop(self.count)
        self.DownBeap(0)
    def DownBeap(self,index):
        """
        Method update Beap after deleting values

        """
        while index <= self.count -1:
            i = int(math.ceil(0.5*(-1+math.sqrt(1.0+8*index))))
            left_son_index = index + i 
            right_son_index = index + i + 1
            l  = False
            r = False
            if left_son_index < self.count:
                left_son_value = self.list[left_son_index]
                l = True
            if right_son_index < self.count:
                right_son_value = self.list[right_son_index]
                r = True
            parent_value = self.list[index]
            if parent_value >= max(left_son_value,right_son_value):
                break
            else:
                if left_son_value >= right_son_value and l == True:
                    self.list[index] = left_son_value
                    self.list[left_son_index] = parent_value
                    index = left_son_index
                elif left_son_value < right_son_value and r == True:
                    self.list[index] = right_son_value
                    self.list[right_son_index] = parent_value
                    index = right_son_index
                else:
                    break
    
    def check(self, val):
        """
        This method wass created to cut code in search method

        """
        sum = 0
        addd = 1
        z = False
        while sum <= val:
            sum += addd
            addd += 1
        if sum == val:
            z = True
        return sum - addd , z
    
    def search(self, value):
        """
        Method searching in O(sqrt(n)) time value on Beap.
        Return: boolean and value (None if False)

        """
        var, boolean = self.check(self.count)
        last_index = None
        if boolean:
            last_index = self.count - 1
        else:
            last_index = var
        current = last_index
        i = int(math.ceil(0.5*(-1+math.sqrt(1+8*current))))
        j = i
        while current != 0:
            if self.list[current] == value:
                return True, current
            elif j == 1 and value < self.list[current] and self.list[current + i] > value:
                break
            elif self.list[current] < value and current + i > self.count -1:
                current -=1
                j -=1
            elif self.list[current] < value and current + i <= self.count -1:
                current += i
                i+= 1
                j-= 1
            else:
                current = current - i
                i -= 1
                j -= 1
            
        return False, None
    def isEmpty(self):
        """
        Information, that Beap is empty or not

        """
        if self.list == []:
            return True
        return False
    def clear(self):
        """
        Removing all values from Beap

        """
        self.list.clear()
        self.count = 0
    def remove(self, value):
        """
        Removing value from Beap, using Search and DownBeap methods.
        Return: 1 if value don't exist in Beap; 0 if everything runs ok.

        """
        boolean, index = self.search(value)
        if not boolean:
            return 1
        self.list.pop(index)
        self.DownBeap(index)
        return 0
    

# T-E-S-T
def main():
    examplelist = [9,7,4,10,2,8,1,3,-5,18,11,15,6,5]
    Beap = BiparentalHeap()
    for i in range(0, len(examplelist)):
        Beap.add_new_value(examplelist[i])
    print(Beap.list)
    Beap.pop()
    print(Beap.list)
    print(Beap.search(8))
    print(Beap.search(22))
    print(Beap.search(-25))
    Beap.remove(10)
    print(Beap.list)
if __name__ == "__main__":
    main()