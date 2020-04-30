import sys

class Node:
	def __init__(self, char = None, frequency = None):
		self.char = char
		self.frequency = frequency

		self.leftChild = None
		self.rightChild = None

class PriorityQueue:
	def __init__(self, array_queue = None):
		if array_queue:
			self.queue = array_queue
		else:
			self.queue = []

	def enqueue(self, string_tuple):
		self.queue.append(string_tuple)

		return True
	
	def getHighestPriority(self):
		least_tuple = None
		for string_tuple in self.queue:
			if least_tuple is None:
				least_tuple = string_tuple
			else:
				if least_tuple[1] > string_tuple[1]:
					least_tuple = string_tuple
		
		if least_tuple:
			self.queue.remove(least_tuple)
			return least_tuple
		else:
			return None
	def getLength(self):
		return len(self.queue)

def generateFrequency(string):
	hash = {}

	for character in string:
		if not character in hash:
			hash[character] = 1
		else:
			hash[character] += 1

	return [(k, v) for k, v in hash.items()] 

def getEncodedData(node, data):
	code_dictionary = getCharCode(node)
	encoded_data = ""

	for char in data:
		encoded_data += code_dictionary[char]['code']

	return encoded_data	

def getCharCode(node, str_code = "", map_code = {}):
	
	if node is None:
		return
	
	if node.char:
		map_code[node.char] = { "frequency": node.frequency, "code": str_code}

	
	getCharCode(node.leftChild, str_code + "0", map_code)
	getCharCode(node.rightChild, str_code + "1", map_code)

	return map_code


def huffman_encoding(data):
	
	# queue with character and frequency pair
	queue = PriorityQueue(generateFrequency(data))

	trees = []

	while queue:
		
		mergeParentNode = Node()

		leastFrequencyChar1 = queue.getHighestPriority()
		leastFrequencyChar2 = queue.getHighestPriority()

		if leastFrequencyChar1 == None and leastFrequencyChar2 == None:
			break

		mergeParentNode.frequency = 0
		if leastFrequencyChar1:
			mergeParentNode.frequency += leastFrequencyChar1[1]
		
		if leastFrequencyChar2:
			mergeParentNode.frequency += leastFrequencyChar2[1]

		mergeParentNode.char = ""

		if leastFrequencyChar1:
			if leastFrequencyChar1[0]:
				mergeParentNode.rightChild = Node(leastFrequencyChar1[0], leastFrequencyChar1[1])
			else:
				mergeParentNode.rightChild = trees.pop(0)

		if leastFrequencyChar2:
			if leastFrequencyChar2[0]:
				mergeParentNode.leftChild = Node(leastFrequencyChar2[0], leastFrequencyChar2[1])
			else:
				mergeParentNode.leftChild = trees.pop(0)

		trees.append(mergeParentNode)

		if queue.getLength() > 0:
			queue.enqueue((mergeParentNode.char, mergeParentNode.frequency))

	return getEncodedData(trees[0], data), trees[0]


def huffman_decoding(encoded_data, root):
	current = root
	result = ''
	
	for code in encoded_data:
		if int(code) == 0:
			current = current.leftChild
		else:
			current = current.rightChild
		if current.leftChild == None and current.rightChild == None:
			result += current.char
			current = root
	
	return result

a_great_sentence = "The bird is the word	"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
