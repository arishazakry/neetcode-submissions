class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dictionary = defaultdict(int)
        for i in nums:
            dictionary[i] += 1

        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))

        only_keys = list(sorted_dict.keys())
        return only_keys[0:k]


