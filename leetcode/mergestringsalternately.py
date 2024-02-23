class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x,y = 0, 0 # set the index that each starts at
        new = [] # sets a list to add letters to
        # here we're setting up a loop that occurs while the variable has a lower value than the length of the word - otherwise it stops.
        while x < len(word1) and y < len(word2): 
            new.append(word1[x]) # first we append to "new" a letter from word1 at the index of x
            new.append(word2[y]) # then we append a letter from word2 at the index of y
            # then we increment both x and y and the loop starts over. checking to see if x and y are < the length of their respective word
            x += 1
            y += 1
        # if the while loop fails and there are still letters in one of the words we append the remainder of those letters to the list of "new" first checking x then y
        new.append(word1[x:])
        new.append(word2[y:])
        # finally we return the "new" list as a joined string using an empty string as the separator - so there are no spaces or weird things.
        return "".join(new)