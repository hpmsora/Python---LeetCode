class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        pointer_dict = self.root
        for index in range(len(word)):
            letter = word[index]
            if letter in pointer_dict:
                pointer_dict = pointer_dict[letter]
            else:
                pointer_dict[letter] = {}
                pointer_dict = pointer_dict[letter]
        pointer_dict["end"] = None

    def search(self, word: str) -> bool:
        pointer_dict = self.root
        for index in range(len(word)):
            letter = word[index]
            if letter in pointer_dict:
                pointer_dict = pointer_dict[letter]
            else:
                return False
        if "end" in pointer_dict:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        pointer_dict = self.root
        for index in range(len(prefix)):
            letter = prefix[index]
            if letter in pointer_dict:
                pointer_dict = pointer_dict[letter]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)