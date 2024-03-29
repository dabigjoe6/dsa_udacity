# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
	def __init__(self, handler):
		# Initialize the node with children as before, plus a handler
		self.children = {}
		self.handler = handler


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
	def __init__(self, root_handler, not_found_handler):
		# Initialize the trie with an root node and a handler, this is the root path or home page node
		self.root = RouteTrieNode(root_handler)
		self.notFoundHandler = not_found_handler

	def insert(self, path, handler):
		# Similar to our previous example you will want to recursively add nodes
		# Make sure you assign the handler to only the leaf (deepest) node of this path

		currentNode = self.root

		for route in path.split('/'):
			if not route in currentNode.children:
				currentNode.children[route] = RouteTrieNode(self.notFoundHandler)
				currentNode = currentNode.children[route]
			else:
				currentNode = currentNode.children[route]
		currentNode.handler = handler

	def find(self, path):
		# Starting at the root, navigate the Trie to find a match for this path
		# Return the handler for a match, or None for no match

		currentNode = self.root

		for route in path.split('/'):
			if not route in currentNode.children:
				return self.notFoundHandler
			else:
				currentNode = currentNode.children[route]

		return currentNode.handler

# The Router class will wrap the Trie and handle 
class Router:
	def __init__(self, root_handler, not_found_handler):
		# Create a new RouteTrie for holding our routes
		# You could also add a handler for 404 page not found responses as well!
		self.routes = RouteTrie(root_handler, not_found_handler)

	def add_handler(self, path, handler):
		# Add a handler for a path
		# You will need to split the path and pass the pass parts
		# as a list to the RouteTrie
		self.routes.insert(path, handler)

	def lookup(self, path):
		# lookup path (by parts) and return the associated handler
		# you can return None if it's not found or
		# return the "not found" handler if you added one
		# bonus points if a path works with and without a trailing slash
		# e.g. /about and /about/ both return the /about handler
		if path == '/':
			return self.routes.root.handler

		if path[-1] == '/':
			path = path[:-1]

		return self.routes.find(path)


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one