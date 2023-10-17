""" Tower of Hanoi - simple solution by Krzysztof Adamczyk """
class Hanoi:
    """
    Methods:
    * __init__()
    * addtoHanoi(val)
    * printHanoi()
    * recursiveHanoi(n, src, tmp, out)

    """
    def __init__(self):
        """
        Constructor creates empty list of lists, which symbolize: input tower, temporary tower and output tower.
        Root is the maximum element in Hanoi input tower

        """
        self.tower = [[], [], []]
        self.root = None
    def addtoHanoi(self, val):
        """
        Method adds new value to Hanoi. Inputted value must be less than the smallest value that already exist in tower.
        Obviously, we can do this with any sort algorithm, but this code is 
        only a real simulation of adding smaller and smaller elements in tower.

        """
        if self.root is None:
            self.root = val
            self.tower[0].append(val)
            return
        if self.tower[0][len(self.tower[0] ) - 1] < val:
            return
        self.tower[0].append(val)
    def printHanoi(self):
        """
        This method makes graphical presentation of situation on towers.

        """
        print("-------------------------")
        print('SRC: ', end="  ")
        print(self.tower[0])
        print("\n TEMP: ", end="  ")
        print(self.tower[1])
        print("\n OUT: ", end="  ")
        print(self.tower[2] )
    def recursiveHanoi(self, n, src = 0, tmp = 1, dst = 2):
        """
        This Method is recursive algorithm of Hanoi towers.
        Input: n - number of elements in source tower,
               src - index of source towers in list
               tmp - index of temporary tower in list
               out - index of output tower in list
        After every operation system is printing situation on towers
        
        """
        if n == 0:
            return
        self.recursiveHanoi(n-1, src, dst, tmp)
        self.tower[dst].append(self.tower[src].pop())
        self.printHanoi()
        self.recursiveHanoi(n-1, tmp, src, dst)

# T - E - S - T
def main():
    hanoi = Hanoi()
    ex_list = [5,4,3,2,1]
    for element in ex_list:
        hanoi.addtoHanoi(element)
    hanoi.printHanoi()
    hanoi.recursiveHanoi(len(ex_list))
if __name__ == "__main__":
    main()
        
