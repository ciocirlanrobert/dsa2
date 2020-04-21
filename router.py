from collections import defaultdict

class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = defaultdict(RouteTrieNode)
        
class RouteTrie:
    def __init__(self, root):
        self.root = RouteTrieNode(root)

    def insert(self, path, handler):
        if len(path) == 1 and path[0] == '':
            return

        current_node = self.root
        for c in path:
            current_node = current_node.children[c]
        current_node.handler = handler

    def find(self, path):
        if len(path) == 1 and path[0] == '':
            return self.root.handler

        current_node = self.root
        for c in path:
            if c not in current_node.children:
                return None
            current_node = current_node.children[c]
        return current_node.handler



class Router:
    def __init__(self, root, no_handler):
        self.router = RouteTrie(root)
        self.no_handler = no_handler

    def add_handler(self, path, handler):
        self.router.insert(self.split_path(path), handler)

    def lookup(self, path):     
        if path is None:
            return self.no_handler

        handler = self.router.find(self.split_path(path))
        if handler is None:
            return self.no_handler
        
        return handler


    def split_path(self, path):
        llist = path.split('/')
        if len(llist) > 1 and llist[-1] == '':
            llist.pop()
        return llist

# Test cases
# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a router
router.add_handler("/games/csgo", "csgo handler")

print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'
print(router.lookup(None)) # should print 'not found handler'
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/games/csgo")) # should print 'csgo handler'
print(router.lookup("games"))#should print not foudn handler
