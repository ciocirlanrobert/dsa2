For this problem I implemented the router using a trie, again.

Complexities:
	=> Time: O(n) ( add_handler, lookup, split_path)
	=> Space: O(path_length * N) where N is the number of handlers in Trie.
