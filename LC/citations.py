class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        citations.reverse()
        for idx, cit in enumerate(citations):
            if cit <= idx:
                return idx
        return len(citations)  