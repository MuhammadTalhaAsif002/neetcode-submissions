class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table={}
        if(len(strs)>1):
            for i in range(len(strs)):
                if ''.join(sorted(strs[i])) in hash_table:
                    hash_table[''.join(sorted(strs[i]))].append(strs[i])
                else:
                    hash_table[''.join(sorted(strs[i]))]=[strs[i]]
            return list(hash_table.values())
        else :
            return list([strs])
            