class TreeNode:
    def __init__(self):
        self.children = dict()
        self.isWords = True

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TreeNode()
                node.children[letter] = child
            node = child
        node.isWords = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node  = self.root
        for letter in word:
            node = node.children.get(letter)
            if not node:
                return False
        return node.isWords

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return False
        return True
