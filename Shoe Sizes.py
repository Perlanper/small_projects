from solution_interface import SolutionInterface
import api

class Solution(SolutionInterface):
    def __init__(self):
        # You can initiate and calculate things here
        self.entrys = api.get_list_length()
        self.names =[]
        self.sizes = []
        
        for i in range(self.entrys): # fills the lists from the api
            self.names.append(api.get_name(i))
            self.sizes.append(api.get_size(i))
        pass

    def popular_size(self):
        """
        Return the most popular shoe size in the customer list.
        
        
        :rtype: int
        """
        # Write your code here
        sizesdict = {}     # will have the form {Size:Count}
        for i in self.sizes:
            if i in sizesdict.keys(): # if element allready exists in dict -> increment
                sizesdict[i] += 1
            else:                   # else element in dict
                sizesdict[i] = 1
        isUnique = 0
        
        for key in sizesdict: # loop the entire dict with keys
            if sizesdict[key] == max(sizesdict.values()):
                isUnique += 1 # if value of the current key has the max value -> increment global variable 
        if isUnique > 1:
            return -1 # if variable is larger than 1 there exists another key with the same value
        else:
            return max(sizesdict, key=sizesdict.get) # else return the most popular size

    def popular_name(self):
        """
        Return the most popular name for the most popular shoe size in the given list.
        
        
        :rtype: str
        """
        # Write your code here
        mostPopularSize = self.popular_size() # calls previous function
        if mostPopularSize == -1: # if it return value = -1 we know that the most popular size is not unique
            return ""

        popularNames = []
        for i in range(len(self.sizes)): # loop thru every index of sizes 
            if self.sizes[i] == mostPopularSize:
                popularNames.append(self.names[i]) #if the index of the currect size is the most popular size we know the index for the name 
        namesdict={} # form {Name:Count}
        for i in popularNames:
            if i in namesdict.keys(): # basically the same thing as in the other function but counting the number of times the names appear
                namesdict[i] += 1
            else:
                namesdict[i] = 1
        isNameUnique = 0
        popularKey = ""
        for key in namesdict: # same thing again to check if there exists names with same count
            if namesdict[key] == max(namesdict.values()):
                isNameUnique += 1
                popularKey = str(key) # here if the name has the max count we save the key 
                #keylist = list(namesdict.keys())
        if isNameUnique > 1:
            return ""
        else:
            return popularKey