class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        my_dict = {
            ("a", "c", "t"): ["act", "cat"]
        }
        """

        my_dict = {}

        for string in strs:
            string_uniq_tulple = tuple(sorted(string))
            str_group = my_dict.setdefault(string_uniq_tulple, [])
            str_group.append(string)

        res = []
        for k, v in my_dict.items():
            res.append(v)

        return res