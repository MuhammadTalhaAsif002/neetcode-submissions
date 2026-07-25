class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        sorted_list=list(sorted(hash_map.items() ,key=lambda x: x[1], reverse=True))
        return [x[0] for x in sorted_list[:k]]
        