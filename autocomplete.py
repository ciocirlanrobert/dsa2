from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    def suffixes(self, suffix = ''):
        string = []
        for char in self.children:
            string += self.children[char].suffixes(suffix + char)
            
        if suffix != '' and self.is_word == True:
            string.append(suffix)
        
        return string

            
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node

    def is_word(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return node.is_word




# Test env setup
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
        
interact(f,prefix='');


print('Test case 1:')
f('antho')#expected logy

print('Test case 2:')
f('')#expected empty


print('Test case 3:')
f('b')#expected not found



