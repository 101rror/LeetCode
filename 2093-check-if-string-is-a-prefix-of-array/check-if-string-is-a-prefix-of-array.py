class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        sub = ""

        for i in words:
            sub += i
            if sub == s:
                return True
            if not s.startswith(sub):
                break

        return False
