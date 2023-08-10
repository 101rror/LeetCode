class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        current = self.trie
        for ch in word:
            if ch not in current:
                current[ch] = dict()
            current = current[ch]
        current['*'] = True

    def _search(self, word: str):
        current = self.trie
        for ch in word:
            if ch not in current:
                return {}
            current = current[ch]
        return current

    def search(self, word: str) -> bool:
        return '*' in self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix) != {}


        


        





        






