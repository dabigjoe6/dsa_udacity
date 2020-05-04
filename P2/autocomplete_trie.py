## Represents a single node in the Trie
class TrieNode:
	def __init__(self):
		## Initialize this node in the Trie
		self.isWord = False
		self.children = {}
	
	def insert(self, char):
		## Add a child node in this Trie
		self.children[char] = TrieNode()

	def suffixes(self, suffix = ''):
		## Recursive function that collects the suffix for 
		## all complete words below this point
		def suffixes_helper(node, char = '', result = []):
			if node.isWord == True:
				result.append(char)
			
			for child in node.children:
				char += child
				suffixes_helper(node.children[child], char)

			return result
		
		return suffixes_helper(self)
		
		
## The Trie itself containing the root node and insert/find functions
class Trie:
	def __init__(self):
		## Initialize this Trie (add a root node)
		self.root = TrieNode()

	def insert(self, word):
		## Add a word to the Trie
		currentNode = self.root
		
		for char in word:
			if char not in currentNode.children:
				currentNode.insert(char)
				currentNode = currentNode.children[char]
			else:
				currentNode = currentNode.children[char]
				
		currentNode.isWord = True        

	def find(self, prefix):
		## Find the Trie node that represents this prefix
		
		currentNode = self.root
		
		for char in prefix:
			if not char in currentNode.children:
				return False
			else:
				currentNode = currentNode.children[char]
		return currentNode

	
MyTrie = Trie()
wordList = [
	"ant", "anthology", "antagonist", "antonym", 
	"fun", "function", "factory", 
	"trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
	MyTrie.insert(word)

prefix = MyTrie.find('f')
# print(prefix.suffixes())
print('\n'.join(prefix.suffixes()))	
