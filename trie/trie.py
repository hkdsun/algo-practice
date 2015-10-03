class TrieNode(object):
    def __init__(self, val):
        self.value = val
        self.children = {}
        self.terminal = False
        """
        Initialize your data structure here.
        """
    def __str__(self):
        if len(self.children)>0:
            return self.value + "-->" + '-'.join(map(lambda c: c.value, self.children))
        else:
            return self.value
    def __repr__(self):
        return self.value
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.terminal = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        if node.terminal:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
        
def print_child(child):
    print child
    if len(child.children) > 0:
        for c in child.children:
            print_child(c)
        

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("app")
trie.insert("apple")
trie.insert("beer")
trie.insert("add")
trie.insert("jam")
trie.insert("rental")

print trie.search("rental")

