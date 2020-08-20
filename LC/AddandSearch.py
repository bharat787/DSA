class TrieNode():
    
    def __init__(self):
        self.childNodes = {}
        self.isEndWord = False
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currNode = self.root
        
        for ch in word:
            node = currNode.childNodes.get(ch, TrieNode())
            currNode.childNodes[ch] = node
            currNode = node
            
        currNode.isEndWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchRecursive(word, self.root, 0)
    
    def searchRecursive(self, word:str, root:TrieNode, index:int) -> bool:
        
        if index == len(word):
            return root.isEndWord
        
        currNode = root
        status = False
        
        if word[index] != '.' and word[index] not in currNode.childNodes:
            return False
        
        if word[index]!= '.':
            return self.searchRecursive(word, currNode.childNodes[word[index]], index+1)
        else:
            for c in currNode.childNodes:
                status = status or self.searchRecursive(word, currNode.childNodes[c], index+1)
            return status
            
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)