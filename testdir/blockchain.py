import hashlib

class Block:

	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()
		self.previous_block = None

	def calc_hash(self):
		sha = hashlib.sha256()

		hash_str = "We are going to encode this string of data!".encode('utf-8')

		sha.update(hash_str)

		return sha.hexdigest()

class BlockChain:

	def __init__(self, block=None):
		self.head = None

	def addBlock(self, block):
		if self.head = None:
			self.head = block
		else:
			block.previous_hash = self.head.hash
			block.previous_block = self.head.previous_block
			self.head = block

