class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        new = [folder[0]]

        for i in range(1, len(folder)):
            last = new[-1] + '/'

            if not folder[i].startswith(last):
                new.append(folder[i])

        return new