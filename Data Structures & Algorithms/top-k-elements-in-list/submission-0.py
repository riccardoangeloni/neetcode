class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        points = dict()

        for i in nums:
            points[i] = points.get(i, 0) + 1

        sorted_keys = sorted(points, key=lambda x: points[x], reverse=True)
        
        return sorted_keys[:k]   
        